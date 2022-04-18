from django.contrib import admin
from import_export.formats.base_formats import XLS, XLSX
from django.utils import timezone

from ..forms.order import OrderForm
from ..resources.order import OrderResource
from .item_inline import ItemInline


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('order_date',)
    list_display = ('order_date',)
    list_filter = ()
    sortable_by = ()
    add_fieldsets = None
    readonly_fields = ('creator', 'updator')

    inlines = (ItemInline,)

    form = OrderForm
    resource_class = OrderResource
    formats = (XLSX,)

    def get_changeform_initial_data(self, request):
        return {
            'order_date': timezone.now().today
        }

    def get_fieldsets(self, request, obj=None):
        if not obj and getattr(self, 'add_fieldsets', None):
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.updator = request.user
        return super().save_model(request, obj, form, change)
