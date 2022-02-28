from django.contrib import admin

from import_export.admin import ImportExportMixin
from .datadictiteminline import DataDictItemInline


class DataDictAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ('code', 'name')
    sortable_by = ()
    list_display = ('code', 'name', 'is_locked')
    list_editable = ('is_locked',)
    inlines = (DataDictItemInline,)
    readonly_fields = ('locked_at',)
