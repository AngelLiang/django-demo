from import_export import resources
from import_export import widgets
from import_export.fields import Field

from ..models import Item
from import_item.mixins.resource import ItemResourceMixin

from django.contrib.auth import get_user_model
User = get_user_model()


class ItemResource(ItemResourceMixin, resources.ModelResource):
    master_id_field = 'order_id'

    id = Field(column_name='ID', attribute='id')
    product_name = Field(
        column_name='名称',
        attribute='product_name',
    )
    price = Field(
        column_name='单价',
        attribute='price',
    )
    quantity = Field(
        column_name='数量',
        attribute='quantity',
    )

    class Meta:
        model = Item
        fields = '__all__'
        import_id_fields = ('id',)
