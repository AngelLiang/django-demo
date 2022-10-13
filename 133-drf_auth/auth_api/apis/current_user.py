from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, permissions

from rest_framework.viewsets import ViewSet

from ..response import success_response
from ..serializers.current_user import (
    CurrentUserSerializer,
)


class CurrentUserView(ViewSet):

    @swagger_auto_schema(
        operation_summary='获取当前用户信息',
        # operation_description='GET /apis/v1/currentUser',
        tags=['用户信息'],
        responses={200: CurrentUserSerializer},
    )
    def current_user_info(self, request, *args, **kwargs):
        """获取当前用户信息"""
        current_user = request.user
        serializer = CurrentUserSerializer(current_user)
        return success_response(
            request,
            data=serializer.data
        )


current_user_info_view = CurrentUserView.as_view({'get': 'current_user_info'})
