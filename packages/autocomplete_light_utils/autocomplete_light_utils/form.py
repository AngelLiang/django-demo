from django import forms
from django.forms import models
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib import admin

from dal import autocomplete


class WrapperFieldsFormMixin(models.ModelForm):

    wrapper_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_fields()

    def initialize_fields(self):
        for name in self.wrapper_fields:
            field = self.declared_fields[name]
            if field.disabled is True:
                # bug: 第二次刷新不起作用
                continue
            if isinstance(field, forms.ModelChoiceField) and isinstance(field.widget, autocomplete.ModelSelect2):
                self.field_add_wrapper(name, field)

    def field_add_wrapper(self, name, formfield):
        if not isinstance(formfield.widget, RelatedFieldWidgetWrapper):
            db_field = self._meta.model._meta.get_field(name)
            related_modeladmin = admin.site._registry.get(db_field.remote_field.model)
            wrapper_kwargs = {}
            if related_modeladmin:
                # request = get_current_request()
                wrapper_kwargs.update(
                    can_add_related=related_modeladmin.has_add_permission(request),
                    can_change_related=related_modeladmin.has_change_permission(request),
                    can_delete_related=related_modeladmin.has_delete_permission(request),
                    can_view_related=related_modeladmin.has_view_permission(request),
                )
            formfield.widget = RelatedFieldWidgetWrapper(
                formfield.widget, db_field.remote_field, related_modeladmin.admin_site, **wrapper_kwargs
            )
