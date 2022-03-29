from django.contrib import admin
from django.utils import timezone

from river_utils.mixins import RiverAdminActionMixin


class TicketAdmin(RiverAdminActionMixin, admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'title',
                    'get_status', 'creator', 'created_at')
    readonly_fields = (
        'order_no', 'creator', 'status', 'get_status',
        'created_at', 'updated_at'
    )
    add_fieldsets = (
        (None, {
            'fields': [
                # 'order_no',
                # 'get_status',
                'order_date',
                'title',
                'content',
                'creator',
                'created_at',
                'updated_at',
            ]}),
    )
    fieldsets = (
        (None, {
            'fields': [
                'order_no',
                'get_status',
                'order_date',
                'title',
                'content',
                'creator',
                'created_at',
                'updated_at',
            ]}),
    )
    change_form_template = 'admin/ticket/ticket/change_form.html'
    object_history_template = 'admin/ticket/ticket/object_history.html'

    def get_changeform_initial_data(self, request):
        return {
            'order_date': timezone.now().date,
            # 'title': '请填写标题',
            # 'content': '请填写内容',
            'creator': request.user,
        }

    def get_status(self, obj):
        return obj.status or '-'
    get_status.short_description = '状态'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        return super().save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        if not obj and hasattr(self, 'add_fieldsets'):
            return self.add_fieldsets
        if obj and hasattr(self, 'unchangeable_fieldsets') and not self.has_change_permission(request, obj):
            return self.unchangeable_fieldsets
        return super().get_fieldsets(request, obj)

    # def has_change_permission(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return super().has_change_permission(request, obj=obj)
    #     if obj and obj.status and obj.status.slug == 'draft':
    #         return super().has_change_permission(request, obj=obj)
    #     return False
