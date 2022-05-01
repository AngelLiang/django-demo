import os
from django.contrib import admin
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import CustomModel
from .models import EmailSyncLog

from .email_send import send_email
from .email_read import read_email
from .exceptions import EmailSyncError


class EmailSyncLogAdmin(admin.ModelAdmin):
    list_display = ('sync_at', 'sync_user')

    change_list_template = 'admin/email_sync/email_sync/change_list.html'

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('upload-data/',
                 self.admin_site.admin_view(self.upload_data_view),
                 name=f'{self.opts.app_label}_{self.opts.model_name}_upload_data'),
            path('download-data/',
                 self.admin_site.admin_view(self.download_data_view),
                 name=f'{self.opts.app_label}_{self.opts.model_name}_download_data'),
        ] + urls

    def upload_data_view(self, request, extra_context=None):
        from_ = os.getenv('MAIL_FROM', 'from')
        to = os.getenv('MAIL_TO', 'to')
        send_email(from_, to, 'subject')
        url = reverse(
            f'admin:{self.opts.app_label}_{self.opts.model_name}_changelist',
            current_app=self.admin_site.name,
        )
        self.message_user(request, '上传成功', messages.SUCCESS)
        return HttpResponseRedirect(url)

    def download_data_view(self, request, extra_context=None):
        try:
            read_email()
        except EmailSyncError as e:
            msg = e.message
            self.message_user(request, msg, messages.ERROR)
        else:
            self.message_user(request, '下载成功', messages.SUCCESS)
        url = reverse(
            f'admin:{self.opts.app_label}_{self.opts.model_name}_changelist',
            current_app=self.admin_site.name,
        )
        return HttpResponseRedirect(url)


admin.site.register(EmailSyncLog, EmailSyncLogAdmin)
admin.site.register(CustomModel)
