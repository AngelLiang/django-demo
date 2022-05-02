from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class EmailSyncLog(models.Model):
    operate_at = models.DateTimeField(_('操作时间'), auto_now_add=True)

    UPLOAD = 'upload'
    DOWNLOAD = 'download'
    OPERATE_TYPE_CHOICES = [
        (UPLOAD, '上传'),
        (DOWNLOAD, '下载'),
    ]
    operate_type = models.CharField(
        _('操作类型'),
        max_length=16,
        choices=OPERATE_TYPE_CHOICES
    )
    operater = models.ForeignKey(
        User,
        verbose_name=_('操作人'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )
    is_success = models.BooleanField(_('操作成功'), default=True)
    md5 = models.CharField(verbose_name='MD5', max_length=128, default='')

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('数据同步历史')
        verbose_name_plural = _('数据同步历史')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_emailsynclog', _('允许添加数据同步历史')),
            ('view_emailsynclog', _('允许查看数据同步历史')),
            ('change_emailsynclog', _('允许修改数据同步历史')),
            ('delete_emailsynclog', _('允许删除数据同步历史')),
            ('import_emailsynclog', _('允许导入数据同步历史')),
            ('export_emailsynclog', _('允许导出数据同步历史')),
        )

    def __str__(self):
        return str(self.operate_at)
