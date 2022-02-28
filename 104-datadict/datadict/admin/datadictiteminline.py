from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from ..models import DataDictItem


class DataDictItemInline(admin.TabularInline):
    model = DataDictItem
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('code', 'label',)
        }),
    )
