from django.db import models


class Product(models.Model):
    name = models.CharField('产品名称', max_length=255)
    price = models.DecimalField('单价', max_digits=11, decimal_places=2)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'

    def __str__(self):
        return f'{self.name}'
