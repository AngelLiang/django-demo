"""
Usage::

    # admin.py
    from django_autocomplete_light_utils.admin import AutocompleteLightModelAdminMixin

    class CustomModelAdmin(AutocompleteLightModelAdminMixin, admin.ModelAdmin)
        pass


    # forms.py
    from django import forms
    from django.utils.translation import ugettext_lazy as _

    from dal import autocomplete

    class CustomModelForm(forms.ModelForm):

        model = forms.ModelChoiceField(
            label=_('一对多模型'),
            queryset=Model.objects.all(),
            required=False,
            widget=autocomplete.ModelSelect2(
                url='admin:{app_label}_{model_name}_autocomplete_light'.format(app_label='app_label', model_name='model_name')
            )
        )

        models = forms.ModelMultipleChoiceField(
            label=_('多对多模型'),
            queryset=Model.objects.all(),
            required=False,
            widget=autocomplete.ModelSelect2Multiple(
                url='admin:{app_label}_{model_name}_autocomplete_light'.format(app_label='app_label', model_name='model_name')
            )
        )

        submodel = forms.ModelChoiceField(
            label=_('联动查询'),
            queryset=Model.objects.filter(is_active=True).all(),
            required=True,
            widget=autocomplete.ModelSelect2(
                url=f'admin:{Model._meta.app_label}_{Model._meta.model_name}_autocomplete_light',
                forward=(forward.Field('model', ),),
            )
        )

        condition = forms.ModelChoiceField(
            label=_('条件查询'),
            queryset=Model.objects.all(),
            required=False,
            widget=autocomplete.ModelSelect2(
                url=f'admin:{Model._meta.app_label}_{Model._meta.model_name}_autocomplete_light',
                forward=(forward.Const(Model.STATUS_01, 'status'),),
            )
        )

        conditions = forms.ModelChoiceField(
            label=_('多条件查询'),
            queryset=Model.objects.all(),
            required=False,
            widget=autocomplete.ModelSelect2(
                url=f'admin:{Model._meta.app_label}_{Model._meta.model_name}_autocomplete_light',
                forward=(forward.Const((Model.STATUS_01, Model.STATUS_02), 'status__in'),),
            )
        )

        class Meta:
            model = CustomModel
            fields = '__all__'

"""
from copy import deepcopy
import logging
from django.contrib import admin
from django.urls import path

from dal import autocomplete

LOGGER = logging.getLogger(__name__)


def modelclass_view_factory(model_admin, request):

    class ModelAutocompleteView(autocomplete.Select2QuerySetView):

        def get_result_value(self, result):
            """Return the value of a result."""
            field = getattr(model_admin, 'autocomplete_light_result_value_field', 'pk')
            return str(getattr(result, field, 'pk'))

        def extract_forwarded(self, sep='|'):
            forwarded = deepcopy(self.forwarded)
            orfilter_dict = {}
            for key, value in self.forwarded.items():
                if sep in key:
                    no, name = key.split(sep)
                    if no not in orfilter_dict:
                        orfilter_dict[no] = {}
                    orfilter_dict[no].update({name: value})
                    del forwarded[key]
            return forwarded, orfilter_dict

        def get_queryset(self):
            force_distinct = False
            if self.forwarded:
                force_distinct = self.forwarded.pop('_force_distinct', False)
                _all = self.forwarded.pop('_all', False)

                forwarded, orfilter_dict = self.extract_forwarded()

                if _all:
                    baseqs = model_admin.model.objects.all()
                else:
                    baseqs = model_admin.get_queryset(request)

                try:
                    qs = baseqs.filter(**forwarded)
                except ValueError as e:
                    LOGGER.error(f'{e}:{forwarded}')
                    qs = baseqs.none()
                for item in orfilter_dict:
                    value = orfilter_dict[item]
                    try:
                        qs |= baseqs.filter(**value)
                    except ValueError as e:
                        LOGGER.error(f'{e}:{item}={value}')
                        continue
            else:
                qs = model_admin.get_queryset(request)

            qs, search_use_distinct = model_admin.get_search_results(request, qs, self.q)
            if search_use_distinct or force_distinct:
                qs = qs.distinct()
            return qs

    return ModelAutocompleteView


class AutocompleteLightModelAdminMixin(admin.ModelAdmin):

    autocomplete_light_result_value_field = 'pk'

    def autocomplete_light_view(self, request):
        return modelclass_view_factory(self, request).as_view()(request)

    def get_urls(self):
        urls = super().get_urls()
        return [
            path('autocomplete-light/', self.admin_site.admin_view(self.autocomplete_light_view),
                 name=f'{self.opts.app_label}_{self.opts.model_name}_autocomplete_light'),
        ] + urls
