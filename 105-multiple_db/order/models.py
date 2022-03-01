from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

from product.models import Product


class Order(models.Model):
    order_date = models.DateField('订单日期')
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, db_constraint=False)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self):
        return f'{self.order_date} by {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单', db_constraint=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品', db_constraint=False)
    quantity = models.PositiveIntegerField('数量', default=0)

    class Meta:
        verbose_name = '订单明细'
        verbose_name_plural = '订单明细'
