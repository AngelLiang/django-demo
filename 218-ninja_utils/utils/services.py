from typing import Dict, List
from utils.errors import NotFoundError


class BaseService:
    Model = None
    AddIn = None
    ListOut = None
    DetailOut = None

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
        obj_list, obj_total = self.paginate_queryset(qs, params)
        obj_list = self.filter_by_params(obj_list, params, filter_keys)
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
        for attr, val in data.items():
            # getattr(obj, attr, None)
            setattr(obj, attr, val)
        return obj.save()

    def delete_by_id(self, id):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        return True

    def add(self, data: Dict):
        # TODO
        obj = self.Model(**data)
        obj.save()
        return obj
