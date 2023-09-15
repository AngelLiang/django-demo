from typing import Dict
from user.models import User
from user.schemas import UserOut
from django.http import Http404


class UserService:
    Model = User
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
        records = [self.ListOut.from_orm(object).dict() for object in object_list]
        # records = object_list
        return records, object_total

    def get_by_id(self, id) -> Dict:
        qs = self.get_queryset()
        object = qs.filter(id=id).first()
        if not object:
            raise Http404()
        return self.DetailOut.from_orm(object).dict()

    def update_by_id(self, id, data) -> Dict:
        qs = self.get_queryset()
        instance = qs.filter(id=id).first()
        if not object:
            raise Http404()
        for attr, value in data.dict().items():
            setattr(instance, attr, value)
        instance.save()

    def delete_by_id(self, id):
        qs = self.get_queryset()
        instance = qs.filter(id=id).first()
        if not object:
            raise Http404()
        instance.delete()
