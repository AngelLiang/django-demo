from django.contrib import admin
from django import forms

from river.models.workflow import Workflow
from river.models.transitionmeta import TransitionMeta
from river.models.transitionapprovalmeta import TransitionApprovalMeta
from django.contrib.auth.models import Permission

# from dal import autocomplete, forward
# from djtoolbox.autocomplete_light_utils import AutocompleteLightModelAdminMixin
# from djtoolbox.admin_auto_filters.filters import AutocompleteFilterFactory


class TransitionApprovalMetaForm(forms.ModelForm):
    workflow = forms.ModelChoiceField(
        label='工作流程',
        queryset=Workflow.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_workflow_autocomplete_light',
        #     # forward=(forward.Const(True, 'is_active'),),
        # )
    )

    transition_meta = forms.ModelChoiceField(
        label='Transition Meta',
        queryset=TransitionMeta.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_transitionmeta_autocomplete_light',
        #     forward=(forward.Field('workflow'),),
        # )
    )

    # permissions = forms.ModelMultipleChoiceField(
    #     label='权限',
    #     queryset=Permission.objects.all(),
    #     required=False,
    #     widget=autocomplete.ModelSelect2Multiple(
    #         url='admin:{app_label}_{model_name}_autocomplete_light'.format(
    #             app_label='auth', model_name='permission')
    #     )
    # )

    class Meta:
        model = TransitionApprovalMeta
        fields = ('name', 'workflow', 'transition_meta', 'permissions', 'groups', 'priority')


class TransitionApprovalMetaAdmin(admin.ModelAdmin):
    list_filter = (
        'workflow',
        # AutocompleteFilterFactory('工作流程', 'workflow', 'admin:river_workflow_autocomplete', True),
    )
    sortable_by = ()
    list_display = ('transition_meta', 'name', 'workflow', 'priority')

    form = TransitionApprovalMetaForm
