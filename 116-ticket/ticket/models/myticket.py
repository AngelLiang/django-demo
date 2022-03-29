from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .ticket import Ticket
# from river.models.fields.state import StateField
from river.models.fields.state import _on_workflow_object_saved, _on_workflow_object_deleted


class MyTicket(Ticket):

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


# 代理模型需要添加下面两个信号处理，否则添加的时候，可能流程状态初始化不成功
post_save.connect(_on_workflow_object_saved, MyTicket, False,
                  dispatch_uid='%s_%s_riverstatefield_post' % (MyTicket, 'status'))
post_delete.connect(_on_workflow_object_deleted, MyTicket, False,
                    dispatch_uid='%s_%s_riverstatefield_post' % (MyTicket, 'status'))
