import os
from datetime import datetime
from django.contrib import admin
from import_export.admin import ImportExportMixin as _ImportExportMixin
from django.http import FileResponse
from django.urls import path
from django.contrib.auth import get_permission_codename
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from import_export.results import RowResult

from django.contrib.admin.models import ADDITION, CHANGE, DELETION, LogEntry, ACTION_FLAG_CHOICES
from django.contrib.contenttypes.models import ContentType


class ImportExportMixin(_ImportExportMixin):
    import_template_name = 'admin/import_export_utils/import.html'
    export_template_name = 'admin/import_export_utils/export.html'

    change_message_map = {
        RowResult.IMPORT_TYPE_NEW: _('通过导入新增。'),
        RowResult.IMPORT_TYPE_UPDATE: _('通过导入修改。'),
        RowResult.IMPORT_TYPE_DELETE: _('通过导入删除。'),
    }

    # to_encoding = 'gbk'
    from_encoding = 'gbk'

    # def get_export_filename(self, request, queryset, file_format):
    #     date_str = datetime.now().strftime('%Y-%m-%d')
    #     filename = "%s-%s.%s" % (self.model._meta.verbose_name_plural,
    #                              date_str,
    #                              file_format.get_extension())
    #     return filename

    def generate_log_entries(self, result, request):
        if not self.get_skip_admin_log():
            # Add imported objects to LogEntry
            logentry_map = {
                RowResult.IMPORT_TYPE_NEW: ADDITION,
                RowResult.IMPORT_TYPE_UPDATE: CHANGE,
                RowResult.IMPORT_TYPE_DELETE: DELETION,
            }
            content_type_id = ContentType.objects.get_for_model(self.model).pk
            for row in result:
                if row.import_type != row.IMPORT_TYPE_ERROR and row.import_type != row.IMPORT_TYPE_SKIP:
                    change_message = self.change_message_map.get(
                        row.import_type, RowResult.IMPORT_TYPE_UPDATE)
                    LogEntry.objects.log_action(
                        user_id=request.user.pk,
                        content_type_id=content_type_id,
                        object_id=row.object_id,
                        object_repr=row.object_repr,
                        action_flag=logentry_map[row.import_type],
                        # change_message=_("%s through import_export" % row.import_type),
                        change_message=change_message,  # 修改导入记录为中文
                    )

    def add_success_message(self, result, request):
        opts = self.model._meta

        success_message = _('导入成功， 新增 {} 条， '
                            '更新 {} 条 {}。').format(result.totals[RowResult.IMPORT_TYPE_NEW],
                                                  result.totals[RowResult.IMPORT_TYPE_UPDATE],
                                                  opts.verbose_name_plural)

        messages.success(request, success_message)


class ImportTemplateDownloadMixin(admin.ModelAdmin):

    def get_import_template_pathfile(self, request):
        """
        example::
            curr_dir = os.path.dirname(os.path.realpath(__file__))
            filepath = os.path.join(curr_dir, '..', 'static', 'admin', self.opts.app_label, self.opts.model_name, '导入模板.xls')
        """

        raise NotImplementedError

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('download-import-template/',
                 self.admin_site.admin_view(self.download_import_template),
                 name=f'{self.opts.app_label}_{self.opts.model_name}_download_import_template')
        ] + urls

    def download_import_template(self, request):
        filepath = self.get_import_template_pathfile(request)
        f = open(filepath, 'rb')
        return FileResponse(f, as_attachment=True, filename=os.path.basename(f.name))

    def has_download_import_template_permission(self, request, obj=None):
        opts = self.opts
        codename = get_permission_codename('download_import_template', opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    def changelist_view(self, request, extra_context=None):
        context = extra_context or {}
        context.update({
            'has_download_import_template_permission': self.has_download_import_template_permission(request),
        })
        return super().changelist_view(request, extra_context)
