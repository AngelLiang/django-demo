from django.contrib import admin

from . import models


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user',)
    list_editable = ('name', 'user',)


admin.site.register(models.Department, DepartmentAdmin)
