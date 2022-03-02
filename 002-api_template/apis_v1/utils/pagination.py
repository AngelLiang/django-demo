from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPageNumberPagination(PageNumberPagination):

    page_query_param = 'currPage'
    page_size_query_param = 'perPage'

    def __init__(self, pagesize=10):
        self.page_size = pagesize

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('code', 2000),
            ('self', self.request.get_full_path()),
            (self.page_query_param, self.page.number),
            (self.page_size_query_param, self.page.paginator.per_page),
            ('total', self.page.paginator.count),
            ('data', data),
        ]))

    def get_results(self, data):
        return data['data']
