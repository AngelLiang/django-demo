from pydantic import BaseModel, Field
from django.contrib.auth import get_user_model
from typing import Generic, TypeVar, Optional
from typing import Dict, List, Optional
import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer
from ninja import Schema, ModelSchema
from pydantic import create_model


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
    return {'hello': 'world!'}


DataT = TypeVar("DataT")


class ResponseModel(BaseModel, Generic[DataT]):
    code: int = Field(..., example=0)
    message: str = Field(..., example="Success")
    data: Optional[DataT] = Field(None)


class Hello(BaseModel):
    hello: str


@api.get("/custom-response", response=ResponseModel[Hello])
def custom_response(request):
    return ResponseModel(code=0, message="successfully", data={'hello': 'world!'})


User = get_user_model()


class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']


# class UserListOut(Schema):
#     class Data(Schema):
#         records: List[UserSchema]
#         total: int

#     code :int
#     message: str
#     data: Data


def make_response_schema(class_name: str, data_schema):
    response_schema_fields = {
        'code': (int, 0),
        'message': (str, 'success'),
        'data': (data_schema, None)
    }
    response_schema = create_model(
        class_name,
        __config__=None,
        __base__=Schema,
        __module__=Schema.__module__,
        __validators__={},
        **response_schema_fields
    )
    return response_schema


def make_records_response_schema(class_name: str, model_schema):
    """
    创建一个如下的类

    from ninja import Schema

    class UserListOut(Schema):
        class Data(Schema):
            records: List[UserSchema]
            total: int

        code :int = 0
        message: str = 'success'
        data: Data

    """

    data_schema_fields = {
        'records': (List[model_schema], None),
        'total': (int, None)
    }
    data_schema = create_model(
        'Data',
        __config__=None,
        __base__=Schema,
        __module__=Schema.__module__,
        __validators__={},
        **data_schema_fields,
    )  # type: ignore

    # response_schema_fields = {
    #     'code': (int, 0),
    #     'message': (str, 'success'),
    #     'data': (data_schema, None)
    # }
    # response_schema = create_model(
    #     class_name,
    #     __config__=None,
    #     __base__=Schema,
    #     __module__=Schema.__module__,
    #     __validators__={},
    #     **response_schema_fields
    # )
    response_schema = make_response_schema(class_name, data_schema)

    return response_schema


UserListOut = make_records_response_schema('UserListOut', UserSchema)


def make_records_response(records, total, code=0, message='success'):
    return {
        'code': code,
        'message': message,
        'data': {
            'records': records,
            'total': total
        }
    }


@api.get('/users', response=UserListOut)
def list_users(request):
    user_list = User.objects.all()
    user_total = user_list.count()
    records = [UserSchema.from_orm(user).dict() for user in user_list]
    return make_records_response(records, user_total)
