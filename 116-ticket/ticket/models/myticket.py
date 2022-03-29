from django.utils.translation import gettext_lazy as _

from .ticket import Ticket
# from river.models.fields.state import StateField


class MyTicket(Ticket):

    # status = StateField(verbose_name=_('流转状态'), editable=False)

    class Meta:
        proxy = True
        managed = False
        verbose_name = _('我的工单')
        verbose_name_plural = _('我的工单')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_myticket', _('允许添加我的工单')),
            ('view_myticket', _('允许查看我的工单')),
            ('change_myticket', _('允许修改我的工单')),
            ('delete_myticket', _('允许删除我的工单')),
            ('import_myticket', _('允许导入我的工单')),
            ('export_myticket', _('允许导出我的工单')),

            # # 流程权限
            # ('open_myticket', _('允许提交工单')),
            # ('resolve_myticket', _('允许处理工单')),
        )
