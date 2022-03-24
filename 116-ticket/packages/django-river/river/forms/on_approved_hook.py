from django import forms
from django.contrib.admin import widgets
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

# from dal import autocomplete, forward

from ..models import OnApprovedHook
from ..models import Workflow
from ..models import TransitionApprovalMeta
from ..models import TransitionApproval
from ..models import Function


class OnApprovedHookForm(forms.ModelForm):
    class Meta:
        model = OnApprovedHook
        fields = '__all__'

    callback_function = forms.ModelChoiceField(
        label=_("回调函数"),
        queryset=Function.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_function_autocomplete_light',
        # )
    )

    workflow = forms.ModelChoiceField(
        label=_("工作流程"),
        queryset=Workflow.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_workflow_autocomplete_light',
        #     # forward=(forward.Field('workflow'),),
        # )
    )

    transition_approval_meta = forms.ModelChoiceField(
        label=_("Transition Approval Meta"),
        queryset=TransitionApprovalMeta.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_transitionapprovalmeta_autocomplete_light',
        #     forward=(forward.Field('workflow'),),
        # )
    )

    transition_approval = forms.ModelChoiceField(
        label=_("Transition Approval"),
        queryset=TransitionApproval.objects.all(),
        required=False,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_transitionapproval_autocomplete',
        #     forward=(forward.Field('workflow'),),
        # )
    )

    # content_type = forms.ModelChoiceField(
    #     label=_("Content Type"),
    #     queryset=ContentType.objects.all(),
    #     required=False,
    #     widget=autocomplete.ModelSelect2(
    #         url='admin:contenttypes_contenttype_autocomplete',
    #     )
    # )

    is_raise_exception = forms.BooleanField(label=_('是否抛出异常'), initial=True)

    callback_function = forms.ModelChoiceField(
        label=_("回调函数"),
        queryset=Function.objects.all(),
        required=True,
        # widget=autocomplete.ModelSelect2(
        #     url='admin:river_function_autocomplete_light',
        # )
    )

    # hook_type = forms.CharField(
    #     label=_('When?'),
    #     required=True,
    #     empty_label=None,
    #     # queryset=WarehouseType.objects.filter(is_active=True).all(),
    #     widget=widgets.AdminRadioSelect(attrs={
    #         'class': 'radiolist inline'
    #     })
    # )
