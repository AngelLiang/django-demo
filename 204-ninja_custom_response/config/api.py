import code
from typing import Dict, List, Optional
from urllib import response
import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer
from ninja import Schema, ModelSchema

class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        # print(response_status, type(data), data)
        # return orjson.dumps({
        #     'code':0,
        #     'message':'操作成功',
        #     'data':data
        # })
        return orjson.dumps(data)

api = NinjaAPI(renderer=ORJSONRenderer())


@api.get("/hello")
def hello(request):
    return {'hello':'world!'}


from django.contrib.auth import get_user_model
User = get_user_model()


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']


class UserListOut(Schema):
    class Data(Schema):
        records: List[UserSchema]
        total: int

    code :int
    message: str
    data: Data


@api.get('/users', response=UserListOut)
def list_users2(request):
    user_list = User.objects.all()
    user_total = user_list.count()
    records = [UserSchema.from_orm(user).dict() for user in user_list]
    return {
        'code': 0,
        'message':'success',
        'data': {
            'records': records,
            'total': user_total
        }
    }
