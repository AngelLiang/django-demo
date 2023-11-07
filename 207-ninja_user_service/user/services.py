from typing import Dict, List
from user.models import User
from user.schemas import UserOut, UserAddIn
from user.schemas import UserBatchAddIn
from django.http import Http404


class UserService:
    Model = User
    AddIn = UserAddIn
    ListOut = UserOut
    DetailOut = UserOut

    def __init__(self, request) -> None:
        self.request = request

    def get_queryset(self):
        return self.Model.objects.get_queryset()

    def get_list_and_total(self, param=None):
        qs = self.get_queryset()
        object_list = qs.all()
        object_total = object_list.count()
        records = [obj for obj in object_list]
        return records, object_total

    def get_by_id(self, id) -> Dict:
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise Http404()
        return obj

    def add_user(self, data: AddIn):
        user = User(username=data.username)  # User is django auth.User
        user.set_password(data.password)
        user.save()

    def batch_add_user(self, payload: List[UserBatchAddIn]):
        obj_list = [User(**data.dict()) for data in payload]
        self.Model.objects.bulk_create(obj_list)

    def update_by_id(self, id, data) -> Dict:
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise Http404()
        for attr, value in data.dict().items():
            setattr(obj, attr, value)
        obj.save()

    def delete_by_id(self, id):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise Http404()
        obj.delete()
