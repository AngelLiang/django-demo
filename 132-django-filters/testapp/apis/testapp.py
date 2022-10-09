from django.urls import path

import rest_framework
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import filters

from drf_yasg.utils import swagger_auto_schema
import django_filters


from ..models import Testapp
from ..serializers.testapp import TestappSerializer
from ..filters.testapp import TestappFilter


class CustomOrderingFilter(filters.OrderingFilter):
    def get_schema_fields(self, view):
        if hasattr(view, 'ordering_fields'):
            self.ordering_description = "可以排序的字段：" + ', '.join(view.ordering_fields)
        return super().get_schema_fields(view)


class TestappOrderingFilter(CustomOrderingFilter):

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        if ordering:
            queryset = queryset.order_by(*ordering)
        # print(queryset)
        return queryset


class TestappSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField(label='标题', required=True)
    intro = serializers.CharField(label='简介', required=False)
    created_at = serializers.DateTimeField(label='创建时间', required=False, read_only=True)
    updated_at = serializers.DateTimeField(label='更新时间', required=False, read_only=True)

    class Meta:
        model = Testapp
        fields = [
            'id',
            'title',
            'intro',
            'created_at',
            'updated_at',
        ]


class TestappViewSet(viewsets.ModelViewSet):

    queryset = Testapp.objects.all()
    filterset_class = TestappFilter
    serializer_class = TestappSerializer
    filter_backends = [
        filters.SearchFilter,
        django_filters.rest_framework.DjangoFilterBackend,
        TestappOrderingFilter,
    ]
    ordering_fields = [
        'id', 'created_at', 'updated_at',
    ]
    # ordering = ['id']
    search_fields = ['title',]


    # for swagger tag
    tags = ['Testapp']

    @swagger_auto_schema(
        tags=tags
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=tags
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=tags
    )
    def retrieve(self, request, pk=None, **kwargs):
        return super().retrieve(request, pk=None, **kwargs)

    @swagger_auto_schema(
        tags=tags
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=tags
    )
    def destroy(self, request, pk=None, **kwargs):
        return super().destroy(request, pk=None, **kwargs)


testapp_list = TestappViewSet.as_view({'get': 'list', 'post': 'create'})
testapp_detail = TestappViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'})


testapp_urls = [
    path('testapp', testapp_list),
    path('testapp/<int:pk>', testapp_detail),
]
