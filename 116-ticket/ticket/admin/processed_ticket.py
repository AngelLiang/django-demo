from django.contrib import admin
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.contrib.contenttypes.models import ContentType

from river.models.transitionapproval import APPROVED
from river.models import TransitionApproval

from ..models import Ticket
from .ticket import TicketAdmin


class ProcessedTicketAdmin(TicketAdmin):
    list_display = ('order_no', 'order_date', 'title', 'get_status', 'creator')

    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        # 获取已处理的工单
        object_ids = TransitionApproval.objects.filter(
            content_type=ContentType.objects.get_for_model(
                self.model.__base__, for_concrete_model=False),
            status=APPROVED,
            transaction_date__isnull=False,
            transactioner=request.user
        ).annotate(
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
