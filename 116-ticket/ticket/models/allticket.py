from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .ticket import Ticket
# from river.models.fields.state import StateField
from river.models.fields.state import _on_workflow_object_saved, _on_workflow_object_deleted


class AllTicket(Ticket):

    class Meta:
        proxy = True
        managed = False
        verbose_name = _('所有工单')
        verbose_name_plural = _('所有工单')
        default_permissions = ()
        permissions = (
            # 功能权限
            # ('add_allticket', _('允许添加所有工单')),
            ('view_allticket', _('允许查看所有工单')),
            # ('change_allticket', _('允许修改所有工单')),
            # ('delete_allticket', _('允许删除所有工单')),
            # ('import_allticket', _('允许导入所有工单')),
            ('export_allticket', _('允许导出所有工单')),

            # # 流程权限
            # ('open_allticket', _('允许提交工单')),
            # ('resolve_allticket', _('允许处理工单')),
        )


# 代理模型需要添加下面两个信号处理，否则添加的时候，可能流程状态初始化不成功
post_save.connect(_on_workflow_object_saved, AllTicket, False,
                  dispatch_uid='%s_%s_riverstatefield_post' % (AllTicket, 'status'))
post_delete.connect(_on_workflow_object_deleted, AllTicket, False,
                    dispatch_uid='%s_%s_riverstatefield_post' % (AllTicket, 'status'))
