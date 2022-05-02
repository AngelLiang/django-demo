from copy import deepcopy
from import_export import resources
from import_export.fields import Field
from django.utils.translation import gettext_lazy as _
from import_export.results import RowResult
from ..utils import get_admin_by_modelclass
from crum import get_current_request


class ModelResourceLogMixin(resources.ModelResource):

    # def after_import_instance(self, instance, new, row_number=None, **kwargs):
    #     self._skip_diff = self._meta.skip_diff
    #     if not self._skip_diff:
    #         original = deepcopy(instance)
    #         self._diff = self.get_diff_class()(self, original, new)

    def before_save_instance(self, instance, using_transactions, dry_run):
        self._is_add = not instance.pk

    def after_save_instance(self, instance, using_transactions, dry_run):
        admin = get_admin_by_modelclass(instance.__class__)
        request = get_current_request()

        # if not self._skip_diff:
        #     self._diff.compare_with(self, instance, dry_run)

        if admin:
            if self._is_add:
                # admin.log_addition(request, instance, {'added': {}})
                admin.log_addition(request, instance, '以导入方式添加。')
            else:
                # admin.log_change(request, instance, {'changed': {'fields': changed_data}})
                admin.log_change(request, instance, '以导入方式修改。')
        super().after_save_instance(instance, using_transactions, dry_run)


class ModelResourceSkipErrorMixin(resources.ModelResource):

    class Meta:
        raise_errors = False

    def import_row(self, row, instance_loader, **kwargs):
        # overriding import_row to ignore errors and skip rows that fail to import
        # without failing the entire import
        import_result = super().import_row(row, instance_loader, **kwargs)
        if import_result.import_type == RowResult.IMPORT_TYPE_ERROR:
            # Copy the values to display in the preview report
            import_result.diff = [row[val] for val in row]
            # Add a column with the error message
            import_result.diff.append('Errors: {}'.format([err.error for err in import_result.errors]))
            # clear errors and mark the record to skip
            import_result.errors = []
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP

        return import_result
