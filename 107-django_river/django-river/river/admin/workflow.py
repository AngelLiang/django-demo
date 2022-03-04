from django import forms
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from river.core.workflowregistry import workflow_registry
from river.models import Workflow

from .workflowinline import TransitionMetaInline, TransitionApprovalMetaInline
from import_export.formats.base_formats import XLSX, JSON

from django.core.exceptions import PermissionDenied
from django.core import serializers
from river.models import State, TransitionMeta

from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportActionModelAdmin

from ..resources import WorkflowResource


def get_workflow_choices():
    def class_by_id(cid): return workflow_registry.class_index[cid]
    result = []
    for class_id, field_names in workflow_registry.workflows.items():
        cls = class_by_id(class_id)
        content_type = ContentType.objects.get_for_model(cls)
        for field_name in field_names:
            result.append(("%s %s" % (content_type.pk, field_name), "%s.%s - %s" %
                          (cls.__module__, cls.__name__, field_name)))
    return result


class WorkflowForm(forms.ModelForm):
    workflow = forms.ChoiceField(choices=[])

    class Meta:
        model = Workflow
        fields = ('workflow', 'initial_state')

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        self.declared_fields['workflow'].choices = get_workflow_choices()
        if instance and instance.pk:
            self.declared_fields['workflow'].initial = "%s %s" % (instance.content_type.pk, instance.field_name)

        super(WorkflowForm, self).__init__(*args, **kwargs)

    def clean_workflow(self):
        if self.cleaned_data.get('workflow') == '' or ' ' not in self.cleaned_data.get('workflow'):
            return None, None
        else:
            return self.cleaned_data.get('workflow').split(" ")

    def save(self, *args, **kwargs):
        content_type_pk, field_name = self.cleaned_data.get('workflow')
        instance = super(WorkflowForm, self).save(commit=False)
        instance.content_type = ContentType.objects.get(pk=content_type_pk)
        instance.field_name = field_name
        return super(WorkflowForm, self).save(*args, **kwargs)


# noinspection PyMethodMayBeStatic
class WorkflowAdmin(ImportExportMixin,
                    ImportExportActionModelAdmin,
                    admin.ModelAdmin):
    form = WorkflowForm
    list_display = ('model_class', 'field_name', 'initial_state')
    search_fields = ['field_name', 'initial_state__label']
    inlines = (TransitionMetaInline, TransitionApprovalMetaInline)
    formats = (JSON,)
    resource_class = WorkflowResource

    def model_class(self, obj):
        cls = obj.content_type.model_class()
        if cls:
            return "%s.%s" % (cls.__module__, cls.__name__)
        else:
            return "Class not found in the workspace"

    def field_name(self, obj):  # pylint: disable=no-self-use
        return obj.workflow.field_name

    # def get_export_data(self, file_format, queryset, *args, **kwargs):
    #     request = kwargs.pop("request")
    #     if not self.has_export_permission(request):
    #         raise PermissionDenied

    #     objects = (
    #         queryset.iterator(),
    #         State.objects.iterator(),
    #         TransitionMeta.objects.iterator(),
    #         TransitionApprovalMeta.objects.iterator(),
    #     )

    #     def get_objects():
    #         for item in objects:
    #             yield from item

    #     data = serializers.serialize('json', get_objects(), use_natural_foreign_keys=True,
    #                                  use_natural_primary_keys=False, indent=2)
    #     export_data = data
    #     return export_data

    # def process_dataset(self, dataset, confirm_form, request, *args, **kwargs):

    #     serializers

    #     res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
    #     resource = self.get_import_resource_class()(**res_kwargs)

    #     imp_kwargs = self.get_import_data_kwargs(request, form=confirm_form, *args, **kwargs)
    #     return resource.import_data(dataset,
    #                                 dry_run=False,
    #                                 raise_errors=True,
    #                                 file_name=confirm_form.cleaned_data['original_file_name'],
    #                                 user=request.user,
    #                                 **imp_kwargs)
