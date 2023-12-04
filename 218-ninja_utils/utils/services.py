from typing import Dict, List, Type
from utils.errors import NotFoundError
from django.db import models
from pydantic import BaseModel

class BaseService:
    Model: Type[models.Model]
    AddIn: Type[BaseModel]
    ListOut: Type[BaseModel]
    DetailOut: Type[BaseModel]

    def __init__(self, request=None) -> None:
        self.request = request

    def get_queryset(self):
        return self.Model.objects.get_queryset()

    def paginate_queryset(self, queryset, params):
        if params is None:
            params = {}
        page = params.get('current', None)
        per_page = params.get('size', None)
        if page and per_page:
            offset = (page - 1) * per_page
            obj_list = queryset[offset: offset + per_page]
            obj_total = queryset.count()
        else:
            obj_list = queryset.all()
            obj_total = obj_list.count()
        return obj_list, obj_total

    def filter_by_params(self, qs, params, filter_keys):
        if filter_keys is None:
            return qs
        for key in filter_keys:
            value = params.get(key)
            if value is not None:
                filter_params = {key: value}
                qs = qs.filter(**filter_params)
        return qs

    def get_list_and_total(self, params: Dict = None, filter_keys: List | None = None):
        qs = self.get_queryset()
        qs = self.filter_by_params(qs, params, filter_keys)
        obj_list, obj_total = self.paginate_queryset(qs, params)
        records = [self.ListOut.from_orm(record).dict() for record in obj_list]
        return records, obj_total

    def get_by_id(self, id):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        return obj

    def get_detail(self, id):
        obj = self.get_by_id(id)
        return self.DetailOut.from_orm(obj).dict()

    def update_by_id(self, id, data):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        return self.handle_update(obj, data)

    def handle_update(self, obj, data):
        for attr, val in data.items():
            setattr(obj, attr, val)
        return obj.save()

    def delete_by_id(self, id):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        self.handle_delete(obj)
        return True

    def handle_delete(self, obj):
        obj.delete()

    def add(self, data: Dict):
        obj = self.Model(**data)
        obj.save()
        return obj
