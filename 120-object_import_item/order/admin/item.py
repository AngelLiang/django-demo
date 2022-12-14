from django.contrib import admin
from import_export.formats.base_formats import XLS, XLSX
from import_export.admin import ImportExportMixin

# from ..forms.order import OrderForm
from ..resources.item import ItemResource
from object_import_item.mixins import ItemImportExportAdminMixin


# ItemImportExportAdminMixin 需要放到 ImportExportMixin 前面
class ItemAdmin(ItemImportExportAdminMixin, ImportExportMixin, admin.ModelAdmin):
    resource_class = ItemResource
    formats = (XLSX,)

    import_redirect_reverse_url = 'admin:order_order_change'
