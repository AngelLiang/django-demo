from rest_framework.response import Response
from rest_framework import authentication, exceptions, permissions, status
from rest_framework.throttling import UserRateThrottle
from rest_framework import filters
from rest_framework import serializers
# import django_filters
from rest_framework.viewsets import ViewSet

from django.http.response import Http404


class BaseAPIView:
    authentication_classes = [
        # authentication.SessionAuthentication,
        # authentication.TokenAuthentication,
        # RemoteUserAuthentication
    ]
    permission_classes = [
        # permissions.IsAuthenticated
    ]
    # pagination_class = CustomPageNumberPagination
    filter_backends = [
        # filters.SearchFilter,
        # django_filters.rest_framework.DjangoFilterBackend,
        # filters.OrderingFilter,
        # CustomOrderingFilter
    ]
    throttle_classes = [UserRateThrottle]

    input_serializer_class = None
    output_serializer_class = None

    def get_serializer_class(self):
        return self.serializer_class

    def get_input_serializer_class(self, *args, **kwargs):
        serializer = self.input_serializer_class(*args, **kwargs)
        return serializer

    def get_model(self):
        return self.queryset.model

    def get_queryset(self):
        return super().get_queryset()

    def handle_validation_error(self, exc):
        """客制化校验失败的返回响应"""
        # from .response import result_fail
        response = Response({
            'code': 0,
            'self': self.request.get_full_path(),
            'errors': exc.get_full_details(),
        })
        return response
        # return result_fail(None, str(exc.get_full_details()), 4001)

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, exceptions.NotAuthenticated):
            """没有认证"""
            auth_header = self.get_authenticate_header(self.request)
            if auth_header:
                exc.auth_header = auth_header
            data = {'code': 0, 'msg': '没有认证', 'data': None}
            response = Response(data, status=status.HTTP_200_OK)
            response.exception = True
            return response
            # return result_fail('Full authentication is required to access this resource', 'token expire', None)
        elif isinstance(exc, exceptions.AuthenticationFailed):
            """认证失败"""
            # exc
            # if len(exc.args) > 0:
            #     resp = exc.args[0]
            #     resp_json = resp.json()
            #     # return result_fail(resp_json['data'], resp_json['msg'], resp_json['errCode'])
            data = {'code': 0, 'msg': '认证失败', 'data': None}
            response = Response(data, status=status.HTTP_200_OK)
            response.exception = True
            return response
        elif isinstance(exc, (exceptions.NotFound, Http404)):
            data = {'code': 0, 'msg': 'NotFound', 'data': None}
            response = Response(data, status=status.HTTP_200_OK)
            response.exception = True
            return response
        elif isinstance(exc, exceptions.PermissionDenied):
            """没有权限"""
            data = {'code': 0, 'msg': '没有权限', 'data': None}
            response = Response(data, status=status.HTTP_200_OK)
            response.exception = True
            return response
        elif isinstance(exc, exceptions.Throttled):
            """超速"""
            wait = exc.wait
            data = {'code': 0, 'msg': f'请求超过了限速。还剩{wait}秒。', 'data': None}
            response = Response(data, status=status.HTTP_200_OK)
            response.exception = True
            return response
        elif isinstance(exc, serializers.ValidationError):
            """校验失败"""
            response = self.handle_validation_error(exc)
            response.exception = True
            return response

        response = super().handle_exception(exc)
        # 无论发生什么错误，强制使用200返回
        response.status_code = status.HTTP_200_OK
        return response
