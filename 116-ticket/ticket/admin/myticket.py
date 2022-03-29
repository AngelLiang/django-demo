
from django.contrib import admin

from ..models import Ticket
from .ticket import TicketAdmin


class MyTicketAdmin(TicketAdmin):
    list_display = ('order_no', 'order_date', 'title', 'get_status', 'created_at')

    def has_change_permission(self, request, obj=None):
        if obj and obj.status == obj.river.status.workflow.initial_state:
            # 初始状态下可以编辑
            return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.status == obj.river.status.workflow.initial_state:
            # 初始状态下可以删除
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request=request).filter(creator=request.user)
        return qs
