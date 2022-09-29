from import_export import resources
from import_export import widgets
from import_export.fields import Field

from ..models import Testapp

from django.contrib.auth import get_user_model
User = get_user_model()


class TestappResource(resources.ModelResource):

    id = Field(column_name='ID', attribute='id')
    name = Field(
        column_name='名称',
        attribute='name',
    )
    creator = Field(
        column_name='创建者',
        attribute='creator',
        widget=widgets.ForeignKeyWidget(User, field='username'),
    )

    class Meta:
        model = Testapp
        fields = '__all__'
        import_id_fields = ('id',)
