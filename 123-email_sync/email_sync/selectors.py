from django.utils import timezone
from typing import Dict, Iterator
from django.db.models.query import QuerySet


def get_sync_data_list(updated_from, updated_to=None) -> Iterator(QuerySet):
    from .models import CustomModel
    if not updated_to:
        updated_to = timezone.now()
    filters = dict(updated_at__gte=updated_from, updated_at__lte=updated_to)
    return [
        CustomModel.objects.filter(**filters).all(),
    ]


def get_sync_data_serializers(objects) -> Dict:
    from django.core import serializers
    if callable(objects):
        objects = objects()
    return serializers.serialize('python', objects, use_natural_foreign_keys=False,
                                 use_natural_primary_keys=False, ensure_ascii=False)
