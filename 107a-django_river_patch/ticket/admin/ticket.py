from django.contrib import admin

from river_patch.mixins.admin_action import RiverAdminActionMixin


class TicketAdmin(RiverAdminActionMixin, admin.ModelAdmin):
    list_display = ('no', 'title', 'status', 'creator')
    readonly_fields = ('creator', 'status')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_change_permission(request, obj=obj)
        if obj and obj.status and obj.status.slug == 'draft':
            return super().has_change_permission(request, obj=obj)
        return False
