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
            object_list = queryset[offset: offset + per_page]
            object_total = queryset.count()
        else:
            object_list = queryset.all()
            object_total = object_list.count()
        return object_list, object_total

    def get_list_and_total(self, params: Dict = None):
        qs = self.get_queryset()
        object_list, object_total = self.paginate_queryset(qs, params)
        records = [self.ListOut.from_orm(record).dict() for record in object_list]
        return records, object_total

    def get_by_id(self, id):
        qs = self.get_queryset()
        instance = qs.filter(id=id).first()
        if not instance:
            raise NotFoundError()
        return instance
        # return self.DetailOut.from_orm(instance).dict()

    def update_by_id(self, id, data) -> Dict:
        qs = self.get_queryset()
        instance = qs.filter(id=id).first()
        if not instance:
            raise NotFoundError()
        # TODO

    def delete_by_id(self, id):
        qs = self.get_queryset()
        instance = qs.filter(id=id).first()
        if not instance:
            raise NotFoundError()
        # TODO

    def add(self, data: Dict):
        # TODO
        instance = self.Model(**data)
        instance.save()
        return instance
