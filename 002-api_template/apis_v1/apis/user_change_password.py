from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, permissions

from .baseviewset import BaseViewSet
from ..utils import responsecode
from ..serializers.user_change_password import (
    UserChangePasswordSerializer,
)


class UserChangePasswordView(BaseViewSet):

    @swagger_auto_schema(
        operation_summary='修改密码',
        # operation_description='POST /apis/v1/changePassword',
        tags=['用户信息'],
        request_body=UserChangePasswordSerializer,
        responses={200: None},
    )
    def user_change_password(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid(raise_exception=False):
            return responsecode.FailResponse.get_response(request, errors=serializer.errors)
        serializer.save()
        return responsecode.SuccessResponse.get_response(request)


user_change_password_view = UserChangePasswordView.as_view({'post': 'user_change_password'})
