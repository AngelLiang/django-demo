from django.contrib import admin
from django.db.models.functions import Cast
from django.db.models import IntegerField

from ..models import Ticket
from .ticket import TicketAdmin


class PendingTicketAdmin(TicketAdmin):
    list_display = ('order_no', 'order_date', 'title', 'get_status', 'creator')

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # 获取待处理的单据
        object_ids = qs.model.river.status.get_available_approvals(
            request.user).annotate(
                object_id_as_integer=Cast(
                    'object_id', output_field=IntegerField()),
        ).values_list('object_id_as_integer', flat=True)
        if not object_ids:
            return qs.none()

        qs = qs.filter(
            id__in=object_ids
        ).all()

        return qs
        # return qs.distinct()
