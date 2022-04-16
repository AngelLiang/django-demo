from django.contrib import admin

from .. import models
from .order import OrderAdmin
from .item import ItemAdmin

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Item, ItemAdmin)
