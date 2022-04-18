from django.urls import reverse
from django.http import HttpResponse
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
                 self.admin_site.admin_view(self.import_template),
                 name='%s_%s_import_template' % self.get_model_info()),
        ]
        return my_urls + urls

    def import_template(self, request, *args, **kwargs):
        formats = self.get_export_formats()
        file_format = formats[0]()

        queryset = self.model.objects.none()
        export_data = self.get_template_data(file_format, queryset, request=request)

        content_type = file_format.get_content_type()
        response = HttpResponse(export_data, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="{}-template.{}"'.format(
            self.model.__name__, file_format.get_extension()
        )
        return response

    def export_action(self, request, *args, **kwargs):
        self.request = request
        return super().export_action(request)

    def get_export_queryset(self, request):
        is_template = request.GET.get('_is_template', None)
        if is_template:
            return self.model.objects.none()
        master_id = request.GET.get('master_id')
        queryset = super().get_export_queryset(request)
        return queryset

    def get_template_data(self, file_format, queryset, *args, **kwargs):
        """
        Returns file_format representation for given queryset.
        """
        request = kwargs.pop("request")

        resource_class = self.get_export_resource_class()
        data = resource_class(**self.get_export_resource_kwargs(request)).export(queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        return export_data
