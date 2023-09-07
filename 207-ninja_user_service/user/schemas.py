from ninja import Schema, ModelSchema
from .models import User

class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']
        