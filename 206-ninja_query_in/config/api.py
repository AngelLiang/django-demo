from typing import Dict, List, Optional
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer
from ninja import Schema, ModelSchema
from ninja import Query

from django.contrib.auth import get_user_model
User = get_user_model()

api = NinjaAPI()


class UserQueryIn(Schema):
    size: int = None
    current: int = None
    search: str = None

class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username', 'first_name', 'last_name']


@api.get('/users', response=List[UserSchema])
def list_users(request, query_in: UserQueryIn = Query({})):
    print(query_in.dict())
    return User.objects.all()
