from django.contrib import admin

from import_export.admin import ImportExportMixin
from import_export.formats.base_formats import XLSX

from ..resources import DataDictItemResource

class DataDictItemAdmin(admin.ModelAdmin):
    search_fields = ('code', 'label')
    sortable_by = ()
    list_display = ('master', 'code', 'label', )
    list_filter = ('master',)

    resource_class = DataDictItemResource
    formats = (XLSX,)
