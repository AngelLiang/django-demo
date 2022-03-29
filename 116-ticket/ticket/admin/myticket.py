
from django.contrib import admin

from ..models import Ticket
from .ticket import TicketAdmin


class MyTicketAdmin(TicketAdmin):
    list_display = ('order_no', 'order_date', 'title', 'status',)

    def get_queryset(self, request):
        qs = super().get_queryset(request=request).filter(creator=request.user)
        return qs
