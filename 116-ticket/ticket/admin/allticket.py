
from django.contrib import admin

from ..models import Ticket
from .ticket import TicketAdmin


class AllTicketAdmin(TicketAdmin):
    list_display = ('order_no', 'order_date', 'title', 'get_status', 'creator')

    def has_change_permission(self, request, obj=None):
        if obj and obj.status == obj.river.status.workflow.initial_state:
            # 初始状态下可以编辑
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request=request)
        return qs
