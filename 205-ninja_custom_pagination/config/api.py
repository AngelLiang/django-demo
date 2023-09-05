from typing import List, Any
from django.core.paginator import Paginator
from ninja import NinjaAPI
from ninja.pagination import paginate, PaginationBase
from ninja import Schema, ModelSchema
from ninja import Field

from django.contrib.auth import get_user_model
User = get_user_model()

api = NinjaAPI()


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']


class CustomPagination(PaginationBase):

    class Input(Schema):
        current: int = Field(default=None, ge=1)
        size: int = Field(default=None, ge=1)


    class Output(Schema):
        records: List[Any] # `items` is a default attribute
        total: int
        size: int = None
        current: int = None

    items_attribute: str = "records"

    def paginate_queryset(self, queryset, pagination: Input, **params):
        page = pagination.current
        per_page = pagination.size
        if page and per_page:
            # 方案一：手动计算
            # offset = (page - 1) * per_page
            # records = queryset[offset : offset + per_page]
            # total = queryset.count()

            # 方案二：django的分页器 https://docs.djangoproject.com/zh-hans/4.2/ref/paginator/#paginator-class
            p = Paginator(queryset, per_page)
            records = p.page(page).object_list
            total = p.count
        else:
            # 没有分页则返回所有数据
            records = queryset
            total = queryset.count()
        return {
            'records': records,
            'total': total,
            'size': per_page,
            'current': page,
            # 'code':2000,
            # 'message':'操作成功',
            # 'data':{

            # }
        }


@api.get('/users', response=List[UserSchema])
@paginate(CustomPagination)
def list_users(request):
    return User.objects.all()
