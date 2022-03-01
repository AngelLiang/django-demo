from django.contrib import admin

from proj.admin import MultiDBModelAdmin
from proj.admin import MultiDBTabularInline

from . import models
from .forms import OrderForm
from .forms import OrderItemForm

class OrderItemInline(MultiDBTabularInline):
    using = 'order_db'
    model = models.OrderItem
    form = OrderItemForm
    extra = 0
    fields = ('product', 'quantity')


class OrderAdmin(MultiDBModelAdmin):
    using = 'order_db'
    list_display = ('__str__', 'order_date')
    inlines = (OrderItemInline,)
    form = OrderForm


admin.site.register(models.Order, OrderAdmin)
