from ninja import Schema, ModelSchema
from user.models import User


class UserAddIn(Schema):
    username: str
    password: str


class UserUpdateIn(Schema):
    first_name: str
    last_name: str


class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']
