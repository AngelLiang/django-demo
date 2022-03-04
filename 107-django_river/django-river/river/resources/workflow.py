from django.db.transaction import savepoint, savepoint_commit, savepoint_rollback
from django.utils.safestring import mark_safe
from import_export.results import RowResult
import tablib
from django.core import serializers
from django.utils.translation import gettext_lazy as _
from import_export.fields import Field
from import_export import resources

from ..models import Workflow
from ..models import State
from ..models import TransitionMeta
from ..models import TransitionApprovalMeta
from ..models import Function, OnApprovedHook, OnCompleteHook, OnTransitHook


class WorkflowResource(resources.ModelResource):

    model = Field()
    name = Field()

    class Meta:
        model = Workflow
        fields = '__all__'
        use_transactions = True

    def export(self, queryset=None, *args, **kwargs):
        if queryset is None:
            queryset = self.get_queryset()
        objects = (
            State.objects.iterator(),  # State 必须排第一位，否则导入会失败
            queryset.iterator(),
            TransitionMeta.objects.iterator(),
            TransitionApprovalMeta.objects.iterator(),
            Function.objects.iterator(),
            OnApprovedHook.objects.iterator(),
            OnCompleteHook.objects.iterator(),
            OnTransitHook.objects.iterator(),
        )

        def get_objects():
            for item in objects:
                yield from item

        ds = tablib.Dataset()
        data = serializers.serialize('python', get_objects(), use_natural_foreign_keys=True,
                                     use_natural_primary_keys=True)
        ds.dict = data
        return ds

    def import_data_inner(self, dataset, dry_run, raise_errors, using_transactions, collect_failed_rows, **kwargs):
        result = self.get_result_class()()
        result.diff_headers = self.get_diff_headers()
        result.total_rows = len(dataset)

        if using_transactions:
            # when transactions are used we want to create/update/delete object
            # as transaction will be rolled back if dry_run is set
            sp1 = savepoint()

        fixture = dataset.dict
        objects = serializers.deserialize(
            'python', fixture, using=None, ignorenonexistent=True, handle_forward_references=True,
        )

        for obj in objects:
            obj.save()
            instance = obj.object
            row_result = self.get_row_result_class()()
            row_result.import_type = RowResult.IMPORT_TYPE_UPDATE
            row_result.diff = [mark_safe(f'{instance.__class__.__name__}'), mark_safe(f'{instance}'), ]

            row_result.object_id = instance.pk
            row_result.object_repr = str(instance)

            result.increment_row_result_total(row_result)
            result.append_row_result(row_result)

        if using_transactions:
            if dry_run or result.has_errors():
                savepoint_rollback(sp1)
            else:
                savepoint_commit(sp1)

        return result
