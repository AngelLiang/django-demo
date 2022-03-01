from django.contrib import admin

from proj.admin import MultiDBModelAdmin

from . import models


class ProductAdmin(MultiDBModelAdmin):
    using = 'primary'


admin.site.register(models.Product, ProductAdmin)
