from django.conf import settings
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import path
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib import messages
from django.contrib.admin.utils import quote

from river.models import TransitionApproval
from river.models import State
# from .signals import pre_approve
# from .signals import post_approve

from ..tables import TransitionApprovalTable
from django.utils.translation import ugettext_lazy as _


class RiverAdminActionMixin(admin.ModelAdmin):

    def get_list_display(self, request):
        self._current_uesr = request.user  # 获取当前用户
        return super().get_list_display(request)

    def river_approve_view(self, request, object_id, next_state_id=None):
        obj = self.get_object(request, object_id)
        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, self.opts, object_id)

        next_state = get_object_or_404(State, pk=next_state_id)

        try:
            obj.river.status.approve(as_user=request.user, next_state=next_state)
            # admin:<app>_<model>_changelist
            self.message_user(request, _('操作成功'), messages.SUCCESS)
            redirect_url = request.GET.get('redirect_url') or reverse(
                f'admin:{self.opts.app_label}_{self.opts.model_name}_changelist')
            return redirect(redirect_url)
        except Exception as e:
            return HttpResponse(e)

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('<int:object_id>/river/approve/<int:next_state_id>/',
                 self.admin_site.admin_view(self.river_approve_view),
                 name=f'{self.opts.app_label}_{self.opts.model_name}_river_approve_view'),
        ] + urls

    def get_action_name(self, transition_approval):
        if transition_approval.name:
            value = transition_approval.name
        else:
            value = f'{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}'
        # print(value)
        return value

    def create_river_action(self, request, obj, transition_approval, redirect_url=None):
        redirect_url = redirect_url or reverse(
            'admin:%s_%s_change' % (self.opts.app_label, self.opts.model_name),
            args=(quote(obj.pk),),
            current_app=self.admin_site.name,
        )
        approve_url = reverse(f'admin:{self.opts.app_label}_{self.opts.model_name}_river_approve_view',
                              kwargs={'object_id': obj.pk,
                                      'next_state_id': transition_approval.transition.destination_state.pk})
        approve_url += f"?&redirect_url={redirect_url}"
        value = self.get_action_name(transition_approval)
        # if transition_approval.name:
        #     value = transition_approval.name
        # else:
        #     value = f'{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}'

        button_class = 'btn btn-default'
        button_onclick = f"""return confirm('是否确定要 {value} ？')"""
        if 'simpleui' in settings.INSTALLED_APPS:
            button_class = 'el-button el-button--primary el-button--small'
            # button_onclick = f"""self.parent.app.$confirm('是否确定要 {value} ？')"""
        from django.middleware.csrf import get_token
        return format_html(f"""
                <form action="{approve_url}" method="POST">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{get_token(request)}"/>
                    <button type="submit" class="{button_class}" onclick="{button_onclick}">
                        {value}
                    </button>
                </form>
            """)

    def create_river_button(self, obj, transition_approval):
        """创建river按钮"""
        approve_url = reverse(f'admin:{self.opts.app_label}_{self.opts.model_name}_river_approve_view',
                              kwargs={'object_id': obj.pk,
                                      'next_state_id': transition_approval.transition.destination_state.pk})
        if 'simpleui' in settings.INSTALLED_APPS:
            value = self.get_action_name(transition_approval)
            return f"""
                <input
                    type="button"
                    style="margin:2px;2px;2px;2px;"
                    class="el-button el-button--primary el-button--small"
                    value="{value}"
                    onclick="location.href=\'{approve_url}\'"
                />
            """
        return f"""
            <input
                type="button"
                style="margin:2px;2px;2px;2px;"
                value="{value}"
                onclick="location.href=\'{approve_url}\'"
            />
        """

    def river_actions(self, obj):
        content = ""
        # 遍历
        for transition_approval in obj.river.status.get_available_approvals(as_user=self._current_uesr):
            content += self.create_river_button(obj, transition_approval)

        return mark_safe(content)
    river_actions.short_description = _('流程操作')

    def get_change_form_template(self):
        template_list = [
            "admin/%s/%s/change_form.html" % (self.opts.app_label, self.opts.model_name),
            "admin/%s/change_form.html" % self.opts.app_label,
            'admin/river_utils/change_form.html',
            "admin/change_form.html"
        ]
        return template_list
    change_form_template = property(get_change_form_template)

    def get_object_history_template(self):
        template_list = [
            "admin/%s/%s/object_history.html" % (self.opts.app_label, self.opts.model_name),
            "admin/%s/object_history.html" % self.opts.app_label,
            'admin/river_utils/object_history.html',
            "admin/object_history.html",
        ]
        return template_list
    object_history_template = property(get_object_history_template)

    def history_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        # 获取对象
        obj = self.get_object(request, object_id)
        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, self.opts, object_id)

        approvals = TransitionApproval.objects.filter(
            workflow_object=obj,
        ).filter(transaction_date__isnull=False).order_by('-transaction_date')

        approvals_table = TransitionApprovalTable(approvals)
        approvals_table.paginate(page=request.GET.get('page', 1), per_page=25)
        extra_context.update({
            'approvals': approvals,
            'approvals_table': approvals_table,
        })

        return super().history_view(request, object_id, extra_context)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        # 获取对象
        obj = self.get_object(request, object_id)
        if obj is None:
            return self._get_obj_does_not_exist_redirect(request, self.opts, object_id)

        riveractions = []
        qs = obj.river.status.get_available_approvals(as_user=request.user)
        for transition_approval in qs:
            riveractions.append(self.create_river_action(request, obj, transition_approval))

        extra_context = extra_context or {}

        extra_context.update(
            {
                'riveractions': riveractions,
            }
        )
        return super().change_view(
            request, object_id, form_url, extra_context
        )
