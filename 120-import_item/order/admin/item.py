from django.contrib import admin
from import_export.formats.base_formats import XLS, XLSX
from import_export.admin import ImportExportMixin

# from ..forms.order import OrderForm
from ..resources.item import ItemResource
from import_item.mixins.admin_item_import import ItemImportAdminMixin


# ItemImportAdminMixin 需要放到 ImportExportMixin 前面
class ItemAdmin(ItemImportAdminMixin, ImportExportMixin, admin.ModelAdmin):
    resource_class = ItemResource
    formats = (XLSX,)

    item_import_redirect_reverse_url = 'admin:order_order_change'
