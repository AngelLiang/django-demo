from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class Testapp(models.Model):
    name = models.CharField(_('名称'), max_length=40)

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    creator = models.ForeignKey(
        User,
        verbose_name=_('创建者'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )
    updater = models.ForeignKey(
        User,
        verbose_name=_('最后修改者'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )

    class Meta:
        verbose_name = _('Testapp')
        verbose_name_plural = _('Testapp')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_testapp', _('允许添加Testapp')),
            ('view_testapp', _('允许查看Testapp')),
            ('change_testapp', _('允许修改Testapp')),
            ('delete_testapp', _('允许删除Testapp')),

            # for django-import-export
            ('import_testapp', _('允许导入Testapp')),
            ('export_testapp', _('允许导出Testapp')),
        )

    def __str__(self):
        return self.name

    def natural_key(self):
        """That method should always return a natural key tuple"""
        return (self.name,)
