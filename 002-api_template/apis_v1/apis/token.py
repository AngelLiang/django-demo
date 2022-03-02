from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication, permissions

from .baseviewset import BaseViewSet
from ..serializers import TokenSerializer
from ..utils import responsecode
from ..serializers.token import (
    TokenSerializer,
    TokenResponseSerializer,
    TokenDestroyResponseSerializer,
)


class TokenView(BaseViewSet):
    authentication_classes = ()
    permission_classes = ()
    throttle_classes = ()
    serializer_class = TokenSerializer

    @swagger_auto_schema(
        operation_summary='登录获取Token',
        # operation_description='POST /apis/v1/token',
        tags=['认证'],
        request_body=TokenSerializer,
        responses={200: TokenResponseSerializer},
    )
    def fetch(self, request, *args, **kwargs):
        """获取token"""
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if not serializer.is_valid(raise_exception=False):
            return responsecode.AuthenticationFailedError.get_response(request, '帐号或密码错误', '帐号或密码错误')
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return responsecode.SuccessResponse.get_response(
            request,
            data={
                'token': token.key,
            }
        )


class TokenDestroyView(BaseViewSet):
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='登出销毁Token',
        # operation_description='DELETE /apis/v1/token',
        tags=['认证'],
        responses={200: TokenDestroyResponseSerializer},
    )
    def destroy(self, request, *args, **kwargs):
        token = request.auth
        if not token:
            return responsecode.FailResponse.get_response(request, devmsg='没有Token')
        token.delete()
        return responsecode.SuccessResponse.get_response(request)


class TokenPingView(BaseViewSet):
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='测试Token',
        # operation_description='DELETE /apis/v1/token',
        tags=['认证'],
        responses={200: TokenDestroyResponseSerializer},
    )
    def ping(self, request, *args, **kwargs):
        # token = request.auth
        # if not token:
        #     return responsecode.FailResponse.get_response(request, devmsg='没有Token')
        return responsecode.SuccessResponse.get_response(request)


fetch_token_view = TokenView.as_view({'post': 'fetch'})
destory_token_view = TokenDestroyView.as_view({'post': 'destroy'})
ping_token_view = TokenPingView.as_view({'get': 'ping'})


