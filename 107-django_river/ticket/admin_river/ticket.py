import river_admin
from ..models import Ticket


class TicketRiverAdmin(river_admin.RiverAdmin):
    name = "Issue Tracking Flow"
    icon = "mdi-ticket-account"
    list_displays = ['pk', 'no', 'subject', 'description', 'status']


river_admin.site.register(Ticket, "status", TicketRiverAdmin)
