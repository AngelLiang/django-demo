from django.http.response import Http404

from rest_framework import views
from rest_framework import authentication, exceptions, permissions
from rest_framework import status
from rest_framework.throttling import UserRateThrottle

from ..utils import responsecode


class BaseAPIView(views.APIView):
    # 认证
    authentication_classes = [
        # authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]
    # 权限
    permission_classes = [permissions.IsAuthenticated]
    # 限速
    throttle_classes = [UserRateThrottle]

    # pagination_class = CustomPageNumberPagination
    # filter_backends = [
    #     filters.SearchFilter,
    #     django_filters.rest_framework.DjangoFilterBackend,
    #     filters.OrderingFilter,
    # ]

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, exceptions.NotAuthenticated):
            auth_header = self.get_authenticate_header(self.request)

            if auth_header:
                exc.auth_header = auth_header

            response = responsecode.NotAuthenticatedError.get_response(self.request)
            response.exception = True
            return response
        elif isinstance(exc, exceptions.AuthenticationFailed):
            response = responsecode.AuthenticationFailedError.get_response(self.request)
            response.exception = True
            return response
        elif isinstance(exc, (exceptions.NotFound, Http404)):
            response = responsecode.NotFoundError.get_response(self.request)
            response.exception = True
            return response
        elif isinstance(exc, exceptions.PermissionDenied):
            response = responsecode.NotFoundError.get_response(self.request)
            response.exception = True
            return response
        elif isinstance(exc, exceptions.Throttled):
            wait = exc.wait
            response = responsecode.ThrottledError.get_response(self.request, f'请求超过了限速。还剩{wait}秒。')
            response.exception = True
            return response

        # response = super().handle_exception(exc)
        # 其他错误
        response = responsecode.ServerError.get_response(self.request, f'{exc}')
        response.exception = True

        response.status_code = status.HTTP_200_OK
        return response
