from django.contrib import admin

from .. import models
from .ticket import TicketAdmin
from .allticket import AllTicketAdmin
from .myticket import MyTicketAdmin
from .pending_ticket import PendingTicketAdmin
from .processed_ticket import ProcessedTicketAdmin

admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.AllTicket, AllTicketAdmin)
admin.site.register(models.MyTicket, MyTicketAdmin)
admin.site.register(models.PendingTicket, PendingTicketAdmin)
admin.site.register(models.ProcessedTicket, ProcessedTicketAdmin)
