from django.contrib.admin.models import ADDITION
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.db.models import OuterRef, Subquery

from ..models import Ticket
from .ticket import TicketAdmin


class MyTicketAdmin(TicketAdmin):
    list_display = ('no', 'title', 'content', 'status',)

    def get_queryset(self, request):
        qs = super().get_queryset().filter(creator=request.user)
        return qs
