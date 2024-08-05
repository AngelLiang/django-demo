from ninja import Schema
from typing import Optional


class PaginationQueryInMixin:
    size: Optional[int] = None
    current: Optional[int] = None


class PaginationQueryIn(Schema, PaginationQueryInMixin):
    pass
