from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Max
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    order_no = models.CharField(_('单据编号'), max_length=20, unique=True)
    order_date = models.DateField(_('单据日期'))
    prefix = models.CharField(_('单号前缀'), max_length=8)
    number = models.PositiveIntegerField(_('单据号数'))

    title = models.CharField(_('标题'), max_length=128)
    content = models.TextField(_('内容'), max_length=1024, default='')
    creator = models.ForeignKey(
        User,
        verbose_name=_('创建者'),
        on_delete=models.CASCADE,
        db_constraint=False,
        related_name='+',
    )

    def __str__(self):
        return self.order_no

    class Meta:
        verbose_name = _('单据')
        verbose_name_plural = _('单据')
        default_permissions = ()
        permissions = (
            ('add_order', _('允许添加单据')),
            ('view_order', _('允许查看单据')),
            ('change_order', _('允许修改单据')),
            ('delete_order', _('允许删除单据')),
        )

    def initialize_prefix(self):
        if not self.prefix:
            self.prefix = 'NO'
            return self.prefix

    def initialize_order_date(self):
        if not self.order_date:
            self.order_date = timezone.now()
            return self.order_date

    def initialize_number(self):
        """
        计算规则：获取相同前缀，相同日期的单据最大的number再+1
        """
        max_number = self.__class__.objects.filter(
            prefix=self.prefix,
            order_date=self.order_date
        ).exclude(pk=self.pk).aggregate(Max('number')).get('number__max') or 0
        self.number = max_number + 1
        return self.number

    def initialize_order_no(self):
        """
        单据编号规则：前缀 + 日期 + 4位单号数
        """
        date = self.order_date.strftime('%y%m%d')
        self.order_no = '{prefix}-{date}-{number:0>4d}'.format(
            prefix=self.prefix,
            date=date,
            number=self.number
        )
        return self.order_no

    def save(self, *args, **kwargs):
        self.initialize_prefix()
        self.initialize_order_date()
        self.initialize_number()
        self.initialize_order_no()
        super().save(*args, **kwargs)
