from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class EmailSyncLog(models.Model):
    sync_at = models.DateTimeField(_('同步时间'), auto_now_add=True)
    sync_user = models.ForeignKey(
        User,
        verbose_name=_('同步人'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )
    md5 = models.CharField(verbose_name='MD5', max_length=128, default='')

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('邮件同步历史')
        verbose_name_plural = _('邮件同步历史')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_emailsynclog', _('允许添加邮件同步历史')),
            ('view_emailsynclog', _('允许查看邮件同步历史')),
            ('change_emailsynclog', _('允许修改邮件同步历史')),
            ('delete_emailsynclog', _('允许删除邮件同步历史')),
            ('import_emailsynclog', _('允许导入邮件同步历史')),
            ('export_emailsynclog', _('允许导出邮件同步历史')),
        )

    def __str__(self):
        return self.sync_at


class CustomModel(models.Model):
    name = models.CharField('名称', max_length=128, default='')
    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('自定义模型')
        verbose_name_plural = _('自定义模型')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_custommodel', _('允许添加自定义模型')),
            ('view_custommodel', _('允许查看自定义模型')),
            ('change_custommodel', _('允许修改自定义模型')),
            ('delete_custommodel', _('允许删除自定义模型')),
        )

    def __str__(self):
        return self.name
