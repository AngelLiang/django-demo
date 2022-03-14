from django.contrib import admin

from .. import models
from .ticket import TicketAdmin
from .myticket import MyTicketAdmin

admin.site.register(models.MyTicket, MyTicketAdmin)
admin.site.register(models.Ticket, TicketAdmin)
