import datetime
from typing import List
from ninja import Schema, ModelSchema
from ninja import Field
from pydantic import validator
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
    date_joined: datetime.datetime = Field(alias='dateJoined')

    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name', 'date_joined']
        allow_population_by_field_name = True
        json_encoders = {
            datetime.datetime: lambda v: v.timestamp(),
        }

    # @validator("date_joined", pre=True, always=True)
    # def format_date_joined(cls, value):
    #     if isinstance(value, datetime.datetime):
    #         # 将datetime对象转换为字符串
    #         formatted_datetime = value.strftime('%Y-%m-%d %H:%M:%S')
    #         print(type(formatted_datetime), formatted_datetime)
    #         return formatted_datetime
    #     return value


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
