from django.contrib import admin


class StateAdmin(admin.ModelAdmin):
    search_fields = ('slug', 'label')
    list_display = ('__str__', 'slug')
