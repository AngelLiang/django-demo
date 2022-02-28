import os
import binascii

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AppToken(models.Model):
    key = models.CharField(_('App Token'), max_length=40, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('所属帐号'),
        related_name='apptokens',
        on_delete=models.CASCADE,
        db_constraint=False,
    )

    name = models.CharField(_('第三方应用名称'), max_length=128)
    memo = models.TextField(_('备注'), max_length=4096, default='', blank=True)
    # is_active = models.BooleanField(_('启用'), default=True)
    # sequence = models.IntegerField(_('排序'), default=0)

    class Meta:
        verbose_name = _('App Token')
        verbose_name_plural = _('App Token')
        # ordering = ('sequence',)
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_apptoken', _('允许添加App Token')),
            ('view_apptoken', _('允许查看App Token')),
            ('change_apptoken', _('允许修改App Token')),
            ('delete_apptoken', _('允许删除App Token')),
        )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.name
