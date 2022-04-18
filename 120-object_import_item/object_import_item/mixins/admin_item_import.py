from django.urls import reverse
from django.http import HttpResponseRedirect
from import_export.signals import post_import


class ItemImportAdminMixin:
    import_template_name = 'admin/import_export/custom_import.html'
    # change_list_template = 'admin/import_export/hide_import_export_change_list.html'

    import_redirect_reverse_url = 'admin:order_order_change'

    def import_action(self, request, *args, **kwargs):
        self.request = request
        return super().import_action(request)

    def get_import_context_data(self, **kwargs):
        data = super().get_import_context_data(**kwargs)
        request = self.request
        master_id = request.GET.get('master_id')
        data['master_id'] = master_id
        data['redirect_url'] = reverse(
            self.import_redirect_reverse_url,
            args=(master_id,),
            current_app=self.admin_site.name)
        return data

    def process_result(self, result, request):
        self.generate_log_entries(result, request)
        self.add_success_message(result, request)
        post_import.send(sender=None, model=self.model)

        url = request.GET.get('redirect_url') or \
            reverse('admin:%s_%s_changelist' % self.get_model_info(),
                    current_app=self.admin_site.name)
        return HttpResponseRedirect(url)

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        kwargs = super().get_import_resource_kwargs(request, *args, **kwargs)
        kwargs.update({'request': request})
        return kwargs

    # def get_import_data_kwargs(self, request, *args, **kwargs):
    #     """
    #     Prepare kwargs for import_data.
    #     """
    #     form = kwargs.get('form')
    #     if form:
    #         kwargs.pop('form')
    #         return kwargs
    #     return {}

    # def process_dataset(self, dataset, confirm_form, request, *args, **kwargs):
    #     res_kwargs = self.get_import_resource_kwargs(request, form=confirm_form, *args, **kwargs)
    #     resource = self.get_import_resource_class()(**res_kwargs)

    #     imp_kwargs = self.get_import_data_kwargs(request, form=confirm_form, *args, **kwargs)
    #     return resource.import_data(dataset,
    #                                 dry_run=False,
    #                                 raise_errors=True,
    #                                 file_name=confirm_form.cleaned_data['original_file_name'],
    #                                 user=request.user,
    #                                 **imp_kwargs)
