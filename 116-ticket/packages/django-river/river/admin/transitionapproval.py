from django.contrib import admin
from django import forms

from river.models.transitionapproval import TransitionApproval

# from dal import forward
# from djtoolbox.admin_auto_filters.filters import AutocompleteFilterFactory
# from djtoolbox.autocomplete_light_utils import AutocompleteLightModelAdminMixin


class TransitionApprovalForm(forms.ModelForm):
    class Meta:
        model = TransitionApproval
        # fields = ('workflow', 'meta', 'content_type', 'object_id', 'transition', 'transactioner', 'transaction_date')
        exclude = ('previous',)


class TransitionApprovalAdmin(admin.ModelAdmin):
    sortable_by = ()
    list_filter = (
        'workflow',
        'transactioner',
        # AutocompleteFilterFactory('工作流程', 'workflow', 'admin:river_workflow_autocomplete', True),
        # AutocompleteFilterFactory(
        #     '处理者', 'transactioner', 'admin:rbac_user_autocomplete_light', True,
        #     # forward=(forward.Const(True, 'is_active'),),
        # ),
        'transaction_date',
        'status',
    )
    readonly_fields = ('get_workflow_object',)
    list_display = ('id', 'workflow', 'meta', 'transactioner', 'transaction_date', 'workflow_object', 'status')

    form = TransitionApprovalForm
