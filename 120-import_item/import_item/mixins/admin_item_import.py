from django.urls import reverse
from django.http import HttpResponseRedirect
from import_export.signals import post_import


class ItemImportAdminMixin:

    import_redirect_reverse_url = 'admin:order_order_change'

    def import_action(self, request, *args, **kwargs):
        self.request = request
        return super().import_action(request)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
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
        return {'request': request}
