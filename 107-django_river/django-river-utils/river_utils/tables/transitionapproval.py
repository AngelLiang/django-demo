import django_tables2 as tables
from django.utils.translation import ugettext_lazy as _

from river.models import TransitionApproval


class TransitionApprovalTable(tables.Table):

    transaction_date = tables.Column(verbose_name=_('日期/时间'))
    transactioner = tables.Column(verbose_name=_('用户'))
    result = tables.Column(verbose_name=_('处理结果'), accessor='transition__destination_state__label')

    class Meta:
        model = TransitionApproval
        template_name = 'django_tables2/semantic.html'
        fields = ('transaction_date', 'transactioner', 'result',)
        attrs = {'style': 'width:100%;'}
