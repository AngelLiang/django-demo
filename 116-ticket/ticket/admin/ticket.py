from django.contrib import admin
from django.utils import timezone

from river_utils.mixins import RiverAdminActionMixin


class TicketAdmin(RiverAdminActionMixin, admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'title', 'status', 'creator')
    readonly_fields = ('order_no', 'creator', 'status')
    fieldsets = (
        (None, {
            'fields': [
                'order_no',
                'status',
                'order_date',
                'title',
                'content',
                'creator',
            ]}),
    )
    # change_form_template = 'admin/ticket/ticket/change_form.html'

    def get_changeform_initial_data(self, request):
        return {
            'order_date': timezone.now().date,
            'title': '请填写标题',
            'content': '请填写内容',
            'creator': request.user,
        }

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
