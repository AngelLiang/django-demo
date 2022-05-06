from dal import widgets
from django.contrib.admin.widgets import AutocompleteSelect as Base
from django import forms
from django.contrib import admin
from django.db.models.fields.related import ForeignObjectRel
from django.db.models.constants import LOOKUP_SEP  # this is '__'
from django.db.models.fields.related_descriptors import ReverseManyToOneDescriptor, ManyToManyDescriptor
from django.forms.widgets import Media, MEDIA_TYPES, media_property
from django.shortcuts import reverse
from django import VERSION as DJANGO_VERSION

from django.conf import settings

import json
from dal_select2.widgets import ModelSelect2

from admin_auto_filters.filters import AutocompleteFilter as _AutocompleteFilter
from admin_auto_filters.filters import _get_rel_model, generate_choice_field


class AutocompleteFilter(_AutocompleteFilter):
    template = 'django-admin-autocomplete-filter-utils/autocomplete-filter.html'
    title = ''
    field_name = ''
    field_pk = 'pk'
    use_pk_exact = True
    is_placeholder_title = True  # change by lzq
    widget_attrs = {}
    rel_model = None
    parameter_name = None
    form_field = forms.ModelChoiceField

    def __init__(self, request, params, model, model_admin, forward=None):
        if self.parameter_name is None:
            self.parameter_name = self.field_name
            if self.use_pk_exact:
                self.parameter_name += '__{}__exact'.format(self.field_pk)
        self.forward = forward
        super(_AutocompleteFilter, self).__init__(request, params, model, model_admin)

        if self.rel_model:
            model = self.rel_model

        if DJANGO_VERSION >= (3, 2):
            remote_field = model._meta.get_field(self.field_name)
        else:
            remote_field = model._meta.get_field(self.field_name).remote_field

        attrs = self.widget_attrs.copy()
        attrs['id'] = 'id-%s-dal-filter' % self.parameter_name
        if self.is_placeholder_title:
            # Upper case letter P as dirty hack for bypass django2 widget force placeholder value as empty string ("")
            # attrs['data-Placeholder'] = self.title
            # change by lzq
            attrs['data-placeholder'] = self.title

        widget = ModelSelect2(
            url=self.get_autocomplete_url(request, model_admin),
            forward=self.forward,
        )

        form_field = self.get_form_field()
        field = form_field(
            queryset=self.get_queryset_for_field(model, self.field_name),
            widget=widget,
            required=False,
        )

        self._add_media(model_admin, widget)

        self.rendered_widget = field.widget.render(
            name=self.parameter_name,
            value=self.used_parameters.get(self.parameter_name, ''),
            attrs=attrs
        )

def AutocompleteFilterFactory(title, base_parameter_name, viewname='', use_pk_exact=False, label_by=str, widget_attrs=None, forward=None):
    """
    An autocomplete widget filter with a customizable title. Use like this:
        AutocompleteFilterFactory('My title', 'field_name')
        AutocompleteFilterFactory('My title', 'fourth__third__second__first')
    Be sure to include distinct in the model admin get_queryset() if the second form is used.
    Assumes: parameter_name == f'fourth__third__second__{field_name}'
        * title: The title for the filter.
        * base_parameter_name: The field to use for the filter.
        * viewname: The name of the custom AutocompleteJsonView URL to use, if any.
        * use_pk_exact: Whether to use '__pk__exact' in the parameter name when possible.
        * label_by: How to generate the static label for the widget - a callable, the name
          of a model callable, or the name of a model field.


    forward 使用示例：

    class UserAdmin(ModelAdmin):
        ...
        list_filter = (
            AutocompleteFilterFactory(
                _('公司'), 'company', 'admin:organ_company_autocomplete_light', True,
                forward=(forward.Const(True, 'is_active'),),
            ),
            AutocompleteFilterFactory(
                _('部门'), 'department', 'admin:organ_department_autocomplete_light', True,
                forward=(forward.Field('company__pk__exact', 'company'), forward.Const(True, 'is_active'),),
            ),
        )

    """

    class NewMetaFilter(type(AutocompleteFilter)):
        """A metaclass for an autogenerated autocomplete filter class."""

        def __new__(cls, name, bases, attrs):
            super_new = super().__new__(cls, name, bases, attrs)
            super_new.use_pk_exact = use_pk_exact
            field_names = str(base_parameter_name).split(LOOKUP_SEP)
            super_new.field_name = field_names[-1]
            super_new.parameter_name = base_parameter_name
            if len(field_names) <= 1 and super_new.use_pk_exact:
                super_new.parameter_name += '__{}__exact'.format(super_new.field_pk)
            return super_new

    class NewFilter(AutocompleteFilter, metaclass=NewMetaFilter):
        """An autogenerated autocomplete filter class."""

        def __init__(self, request, params, model, model_admin):
            self.rel_model = _get_rel_model(model, base_parameter_name)
            self.form_field = generate_choice_field(label_by)
            self.title = title
            self.widget_attrs = widget_attrs or {}
            super().__init__(request, params, model, model_admin, forward)

        def get_autocomplete_url(self, request, model_admin):
            if viewname == '':
                return super().get_autocomplete_url(request, model_admin)
            else:
                return reverse(viewname)

    return NewFilter
