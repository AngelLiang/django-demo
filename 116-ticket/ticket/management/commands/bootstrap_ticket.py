from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand
from django.db import transaction
from river.models import TransitionApprovalMeta

from ticket.models import Ticket

DRAFT = 'draft'
APPROVING = 'approving'
PASS = 'pass'
NOPASS = 'nopass'


class Command(BaseCommand):
    help = 'Bootstrapping database with necessary items'

    @transaction.atomic()
    def handle(self, *args, **options):
        from river.models import State, Workflow, TransitionMeta
        from django.contrib.contenttypes.models import ContentType

        proposer, _ = Group.objects.update_or_create(name="工单申请")
        approver, _ = Group.objects.update_or_create(name="工单审批")

        ticket_content_type = ContentType.objects.get_for_model(Ticket)

        draft_state, _ = State.objects.update_or_create(slug=DRAFT, defaults={'label': '草稿'})
        approving_state, _ = State.objects.update_or_create(slug=APPROVING, defaults={'label': '审批中'})
        pass_state, _ = State.objects.update_or_create(slug=PASS, defaults={'label': '已通过'})
        nopass_state, _ = State.objects.update_or_create(slug=NOPASS, defaults={'label': '未通过'})

        workflow = Ticket.river.status.workflow \
                   or Workflow.objects.create(content_type=ticket_content_type, field_name="status", initial_state=draft_state)

        # 删除所有流程数据
        workflow.transition_approvals.filter(workflow=workflow).all().delete()
        workflow.transitions.filter(workflow=workflow).all().delete()
        workflow.transition_approval_metas.filter(workflow=workflow).all().delete()
        workflow.transition_metas.filter(workflow=workflow).all().delete()

        draft_to_approving, _ = TransitionMeta.objects.get_or_create(workflow=workflow, source_state=draft_state, destination_state=approving_state)
        approving_to_pass, _ = TransitionMeta.objects.get_or_create(workflow=workflow, source_state=approving_state, destination_state=pass_state)
        approving_to_nopass, _ = TransitionMeta.objects.get_or_create(workflow=workflow, source_state=approving_state, destination_state=nopass_state)
        nopass_to_draft, _ = TransitionMeta.objects.get_or_create(workflow=workflow, source_state=nopass_state, destination_state=draft_state)
        approving_to_draft, _ = TransitionMeta.objects.get_or_create(workflow=workflow, source_state=approving_state, destination_state=draft_state)


        draft_to_approving_rule, _ = TransitionApprovalMeta.objects.get_or_create(workflow=workflow, transition_meta=draft_to_approving, priority=0, defaults={'name': '提交'})
        draft_to_approving_rule.groups.set([proposer])

        approving_to_pass_rule, _ = TransitionApprovalMeta.objects.get_or_create(workflow=workflow, transition_meta=approving_to_pass, priority=0, defaults={'name': '通过'})
        approving_to_pass_rule.groups.set([approver])

        approving_to_nopass_rule, _ = TransitionApprovalMeta.objects.get_or_create(workflow=workflow, transition_meta=approving_to_nopass, priority=0, defaults={'name': '拒绝'})
        approving_to_nopass_rule.groups.set([approver])

        nopass_to_draft_rule, _ = TransitionApprovalMeta.objects.get_or_create(workflow=workflow, transition_meta=nopass_to_draft, priority=0, defaults={'name': '重做'})
        nopass_to_draft_rule.groups.set([approver])

        approving_to_draft_rule, _ = TransitionApprovalMeta.objects.get_or_create(workflow=workflow, transition_meta=approving_to_draft, priority=0, defaults={'name': '撤回'})
        approving_to_draft_rule.groups.set([proposer])

        self.stdout.write(self.style.SUCCESS('Successfully bootstrapped the ticket workflow '))
