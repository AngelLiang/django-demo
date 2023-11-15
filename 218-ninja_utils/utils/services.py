from typing import Dict
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

    def get_list_and_total(self, params: Dict = None):
        qs = self.get_queryset()
        obj_list, obj_total = self.paginate_queryset(qs, params)
        records = [self.ListOut.from_orm(record).dict() for record in obj_list]
        return records, obj_total

    def get_by_id(self, id):
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        return obj
        # return self.DetailOut.from_orm(obj).dict()

    def update_by_id(self, id, data) -> Dict:
        qs = self.get_queryset()
        obj = qs.filter(id=id).first()
        if not obj:
            raise NotFoundError()
        return True

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
