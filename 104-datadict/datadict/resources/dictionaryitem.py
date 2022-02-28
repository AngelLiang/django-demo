from django.utils.translation import gettext_lazy as _
from import_export.fields import Field
from import_export import resources, widgets

from ..models import DataDict, DataDictItem
from .utils import AutoCreateForeginKeyWidget


class DataDictItemResource(resources.ModelResource):

    master = Field(
        column_name=_('数据字典'),
        attribute='master',
        widget=AutoCreateForeginKeyWidget(DataDict, field='code')
    )

    code = Field(
        column_name=_('编码'),
        attribute='code',
    )

    label = Field(
        column_name=_('标签'),
        attribute='label',
    )

    class Meta:
        model = DataDictItem
        fields = ('master', 'code', 'label')
        import_id_fields = ('master', 'code')
