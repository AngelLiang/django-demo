from django.contrib import admin

from . import models


class ProductAdmin(admin.ModelAdmin):
    using = 'primary'


product_adminsite = admin.AdminSite('product')
product_adminsite.register(models.Product, ProductAdmin)
