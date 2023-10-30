from typing import List
from ninja import Schema, ModelSchema
from ninja import Field
from user.models import User


class UserAddIn(Schema):
    username: str
    password: str


class UserBatchAddIn(Schema):
    username: str
    password: str


class UserUpdateIn(Schema):
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')


class UserOut(ModelSchema):
    first_name: str = Field(None, alias='firstName')
    last_name: str = Field(None, alias='lastName')

    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']
        allow_population_by_field_name = True


class UserDetailResponseOut(Schema):
    code: int = 0
    message: str = "success"
    data: UserOut


class UserListRecordOut(Schema):
    records: List[UserOut]
    total: int = 0


class UserListResponseOut(Schema):
    code: int = 0
    message: str = "success"
    data: UserListRecordOut
