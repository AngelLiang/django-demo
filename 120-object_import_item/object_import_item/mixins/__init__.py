from .admin_item_export import ItemExportAdminMixin
from .admin_item_import import ItemImportAdminMixin


class ItemImportExportAdminMixin(ItemImportAdminMixin, ItemExportAdminMixin):
    pass
