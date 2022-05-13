from django.utils.translation import gettext_lazy as _

from .ticket import Ticket


class MyTicket(Ticket):

    class Meta:
        proxy = True
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
            # ('resovle_myticket', _('允许处理工单')),
        )
