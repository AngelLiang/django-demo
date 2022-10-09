from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import NumberFilter
from django_filters.rest_framework import CharFilter

from ..models import Testapp


class TestappFilter(FilterSet):
    id = NumberFilter(field_name='id')
    ids = CharFilter(label='ids', method='filter_ids', help_text='1,2,3')
    title = CharFilter(label='title', field_name='title')

    class Meta:
        model = Testapp
        fields = [
            'id',
            'ids',
            'title',
        ]

    def filter_ids(self, queryset, name, value):
        return queryset.filter(id__in=value.split(','))
