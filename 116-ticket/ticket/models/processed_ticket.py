from django.utils.translation import gettext_lazy as _
from .ticket import Ticket


class ProcessedTicket(Ticket):

    class Meta:
        proxy = True
        managed = False
        verbose_name = _('已处理的工单')
        verbose_name_plural = _('已处理的工单')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_processedticket', _('允许添加已处理的工单')),
            ('view_processedticket', _('允许查看已处理的工单')),
            ('change_processedticket', _('允许修改已处理的工单')),
            ('delete_processedticket', _('允许删除已处理的工单')),
            ('import_processedticket', _('允许导入已处理的工单')),
            ('export_processedticket', _('允许导出已处理的工单')),
        )
