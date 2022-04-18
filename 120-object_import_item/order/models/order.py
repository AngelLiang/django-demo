from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    order_date = models.DateField('订单日期')

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    creator = models.ForeignKey(
        User,
        verbose_name=_('创建者'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )
    updator = models.ForeignKey(
        User,
        verbose_name=_('最后修改者'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )

    class Meta:
        verbose_name = _('订单')
        verbose_name_plural = _('订单')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_order', _('允许添加订单')),
            ('view_order', _('允许查看订单')),
            ('change_order', _('允许修改订单')),
            ('delete_order', _('允许删除订单')),
            ('import_order', _('允许导入订单')),
            ('export_order', _('允许导出订单')),
        )

    def __str__(self):
        return str(self.order_date)

    def natural_key(self):
        """That method should always return a natural key tuple"""
        return (self.order_date,)
