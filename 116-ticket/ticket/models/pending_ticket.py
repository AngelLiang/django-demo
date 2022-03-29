from django.utils.translation import gettext_lazy as _
from .ticket import Ticket


class PendingTicket(Ticket):

    class Meta:
        proxy = True
        managed = False
        verbose_name = _('待处理的工单')
        verbose_name_plural = _('待处理的工单')
        default_permissions = ()
        permissions = (
            # 功能权限
            # ('add_pendingticket', _('允许添加待处理的工单')),
            ('view_pendingticket', _('允许查看待处理的工单')),
            # ('change_pendingticket', _('允许修改待处理的工单')),
            # ('delete_pendingticket', _('允许删除待处理的工单')),
            # ('import_pendingticket', _('允许导入待处理的工单')),
            ('export_pendingticket', _('允许导出待处理的工单')),
        )
