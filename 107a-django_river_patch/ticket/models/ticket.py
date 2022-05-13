from django.utils.html import format_html
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from river.models.fields.state import StateField
from river.signals import pre_approve, post_approve
from django.dispatch import receiver

from django.contrib.auth import get_user_model
User = get_user_model()


class Ticket(models.Model):
    """工单"""
    no = models.CharField(_('工单号'), max_length=50, default=uuid.uuid4,
                          null=False, blank=False, editable=False,
                          unique=True)
    title = models.CharField(_('标题'), max_length=100, null=False, blank=False)
    content = models.TextField(
        _('详情'), max_length=1024, default='', blank=True)

    status = StateField(verbose_name=_('状态'), editable=False)

    creator = models.ForeignKey(
        User,
        verbose_name=_('创建者'),
        on_delete=models.CASCADE,
        db_constraint=False,
        related_name='+',
    )

    def natural_key(self):
        return (self.no,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('工单')
        verbose_name_plural = _('工单')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_ticket', _('允许添加工单')),
            ('view_ticket', _('允许查看工单')),
            ('change_ticket', _('允许修改工单')),
            ('delete_ticket', _('允许删除工单')),
            ('import_ticket', _('允许导入工单')),
            ('export_ticket', _('允许导出工单')),

            # 流程权限
            ('open_ticket', _('允许提交工单')),
            ('resovle_ticket', _('允许处理工单')),
        )

    def get_creator_from_logentry(self):
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.admin.models import LogEntry, ADDITION
        from django.contrib.auth import get_user_model
        User = get_user_model()
        content_type = ContentType.objects.get_for_model(
            self, for_concrete_model=False)
        # content_type = ContentType.objects.get_by_natural_key()
        user = User.objects.filter(
            logentry__content_type=content_type,
            logentry__object_id=self.pk,
            logentry__action_flag=ADDITION
        ).first()
        return user
    get_creator_from_logentry.short_description = _('创建者')

    # def get_status_tag(self):
    #     if self.status.slug == 'draft':
    #         return format_html(f'<div class="el-tag el-tag--info">{self.status}</div>')
    #     elif self.status.slug == 'resovled':
    #         return format_html(f'<div class="el-tag el-tag--warning">{self.status}</div>')
    #     elif self.status.slug == 'closed':
    #         return format_html(f'<div class="el-tag el-tag--success">{self.status}</div>')
    #     elif self.status.slug in ('open', 're-open'):
    #         return format_html(f'<div class="el-tag el-tag--danger">{self.status}</div>')
    #     return format_html(f'<div class="el-tag el-tag--info">{self.status}</div>')
    # get_status_tag.short_description = _('状态')
    # get_status_tag.allow_tags = True


@receiver(pre_approve, sender=Ticket)
def Ticket_pre_approve(sender, workflow_object, field_name, transition_approval, **kwargs):
    # print((sender, workflow_object, field_name, transition_approval))
    destination_state = transition_approval.transition.destination_state
    # print(destination_state)
    # raise ValueError('提交失败')
