from django.db import models
from django.utils.translation import gettext_lazy as _


class AliyunSendSms(models.Model):
    name = models.CharField(_('模板名称'), max_length=40)

    template_code = models.CharField(_('模板CODE'), max_length=40)
    template_param = models.TextField(_('模板参数'))

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        db_table = 'aliyun_sendsms'
        verbose_name = _('阿里云短信模板')
        verbose_name_plural = _('阿里云短信模板')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_aliyunsendsms', _('允许添加阿里云短信模板')),
            ('view_aliyunsendsms', _('允许查看阿里云短信模板')),
            ('change_aliyunsendsms', _('允许修改阿里云短信模板')),
            ('delete_aliyunsendsms', _('允许删除阿里云短信模板')),

            # for django-import-export
            ('import_aliyunsendsms', _('允许导入阿里云短信模板')),
            ('export_aliyunsendsms', _('允许导出阿里云短信模板')),
        )

    def __str__(self):
        return self.name

    def natural_key(self):
        """That method should always return a natural key tuple"""
        return (self.template_code,)
