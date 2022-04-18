from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


class Item(models.Model):
    order = models.ForeignKey(
        'Order',
        verbose_name=_('订单'),
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    product_name = models.CharField(verbose_name=_('商品名称'), max_length=20)
    price = models.DecimalField(verbose_name=_('单价'), max_digits=14, decimal_places=2)
    quantity = models.DecimalField(verbose_name=_('数量'), max_digits=14, decimal_places=2)

    class Meta:
        verbose_name = _('订单明细')
        verbose_name_plural = _('订单明细')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_item', _('允许添加订单明细')),
            ('view_item', _('允许查看订单明细')),
            ('change_item', _('允许修改订单明细')),
            ('delete_item', _('允许删除订单明细')),
            ('import_item', _('允许导入订单明细')),
            ('export_item', _('允许导出订单明细')),
        )

    def __str__(self):
        return str(self.order)
