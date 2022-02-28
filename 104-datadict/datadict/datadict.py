from django import forms
from django.contrib.admin import widgets


def get_datadictitem(code):
    from datadict.models import DataDictItem
    from django.db.utils import OperationalError, ProgrammingError
    try:
        # return tuple([(item.code, item.label) for item in DictionaryItem.objects.filter(master__code__exact=code)])
        return DataDictItem.objects.filter(master__code__exact=code).values_list('code', 'label').all()
    # except (OperationalError, ProgrammingError):
    except Exception:
        return None


class DataDictItemChoiceField(forms.ChoiceField):
    """
        tp = DataDictItemChoiceField(
            label=_('申请类型'),
            code='application_type',

            required=True,
        )
    """

    def __init__(self, *, code=None, widget=None, **kwargs):
        if widget is None:
            widget = widgets.AdminRadioSelect(attrs={
                'class': 'radiolist inline'
            })
        super().__init__(choices=lambda: get_datadictitem(code), widget=widget, **kwargs)


class DataDictItemModelChoiceField(forms.ModelChoiceField):
    """
        tp = DataDictItemModelChoiceField(
            label=_('申请类型'),
            code='application_type',
            required=True,
        )
    """

    def __init__(self, *, code=None, widget=None, **kwargs):
        if widget is None:
            widget = widgets.AdminRadioSelect(attrs={
                'class': 'radiolist inline'
            })
        from datadict.models import DataDictItem
        queryset = DataDictItem.objects.filter(master__code__exact=code).all()
        to_field_name = 'code'
        initial = kwargs.get('initial', None)
        # initial = queryset.first()
        empty_label = kwargs.get('empty_label', None)
        super().__init__(queryset, widget=widget, to_field_name=to_field_name, initial=initial, empty_label=empty_label, **kwargs)

    def label_from_instance(self, obj):
        return obj.label
