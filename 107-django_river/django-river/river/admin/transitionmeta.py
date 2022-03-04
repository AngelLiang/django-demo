from django import forms
from django.contrib import admin

from river.models import TransitionMeta
# from djtoolbox.autocomplete_light_utils import AutocompleteLightModelAdminMixin
# from djtoolbox.admin_auto_filters.filters import AutocompleteFilterFactory


class TransitionMetaForm(forms.ModelForm):
    class Meta:
        model = TransitionMeta
        fields = ('workflow', 'source_state', 'destination_state')


class TransitionMetaAdmin(admin.ModelAdmin):
    list_filter = (
        'workflow',
        # AutocompleteFilterFactory('工作流程', 'workflow', 'admin:river_workflow_autocomplete', True),
    )
    sortable_by = ()
    list_display = ('workflow', 'source_state', 'destination_state')

    form = TransitionMetaForm
