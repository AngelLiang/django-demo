from django import forms
from django.contrib import admin

from river.models import Transition
# from djtoolbox.autocomplete_light_utils import AutocompleteLightModelAdminMixin
# from djtoolbox.admin_auto_filters.filters import AutocompleteFilterFactory


class TransitionForm(forms.ModelForm):
    class Meta:
        model = Transition
        fields = ('workflow', 'source_state', 'destination_state')


class TransitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'workflow', 'source_state', 'destination_state')
    form = TransitionForm
    list_filter = (
        'workflow',
        # AutocompleteFilterFactory('工作流程', 'workflow', 'admin:river_workflow_autocomplete', True),
    )
