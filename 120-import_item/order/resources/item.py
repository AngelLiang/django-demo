from doctest import master
from import_export import resources
from import_export import widgets
from import_export.fields import Field

from ..models import Item

from django.contrib.auth import get_user_model
User = get_user_model()


class ItemResource(resources.ModelResource):

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

    def __init__(self, request):
        self.request = request
        super().__init__()

    def get_master_id(self):
        return self.request.GET.get('master_id')

    def init_instance(self, row=None):
        instance = super().init_instance(row)
        instance.order_id = self.get_master_id()
        return instance

    # def get_instance(self, instance_loader, row):
    #     master = get_master(StockIn)
    #     location = self.fields['location'].clean(row)
    #     product = self.fields['product'].clean(row)
    #     measure = self.fields['measure'].clean(row)
    #     try:
    #         # 以 master warehouse location product measure 作为唯一键判断
    #         return self.get_queryset().get(
    #             master=master,
    #             warehouse=master.warehouse,
    #             location=location,
    #             product=product,
    #             measure=measure
    #         )
    #     except self._meta.model.DoesNotExist:
    #         return None
