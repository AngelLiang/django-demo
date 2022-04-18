from django.urls import reverse
from django.http import HttpResponseRedirect
from import_export.signals import post_import
from django.urls import path


class ItemExportAdminMixin:

    def get_model_info(self):
        app_label = self.model._meta.app_label
        return (app_label, self.model._meta.model_name)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-template/',
                 self.admin_site.admin_view(self.export_action),
                 name='%s_%s_import_template' % self.get_model_info()),
        ]
        return my_urls + urls

    def export_action(self, request, *args, **kwargs):
        self.request = request
        return super().export_action(request)

    def get_export_queryset(self, request):
        master_id = request.GET.get('master_id')
        queryset = super().get_export_queryset(request)
        return queryset
