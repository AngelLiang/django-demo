from django.contrib import admin

from ..models import Item


class ItemInline(admin.TabularInline):
    """
    admin.TabularInline: 平行的表格
    admin.StackedInline: 垂直的表格
    """
    model = Item
    extra = 0
    fields = ('product_name', 'price', 'quantity')
    readonly_fields = fields
