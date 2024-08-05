from django.conf import settings
from ninja import NinjaAPI
from ninja.security import HttpBearer
import logging

from user.errors import EmptyToken, ExpiredToken, InvalidToken

logger = logging.getLogger('auth')


def init_api_auth(api: NinjaAPI):
    @api.exception_handler(EmptyToken)
    def on_empty_token(request, exc):
        return api.create_response(
            request,
            {
                'code': 401,
                "message": exc.message,
                'data': {}
            },
            status=200
        )

    @api.exception_handler(ExpiredToken)
    def on_expired_token(request, exc):
        return api.create_response(
            request,
            {
                'code': 401,
                "message": exc.message,
                'data': {}
            },
            status=200
        )

    @api.exception_handler(InvalidToken)
    def on_invalid_token(request, exc):
        return api.create_response(
            request,
            {
                'code': 401,
                "message": exc.message,
                'data': {}
            },
            status=200
        )


class AuthBearer(HttpBearer):

    def __call__(self, request):
        """重写该方法，改为如果头部没有配置则抛出异常"""
        headers = request.headers
        auth_value = headers.get(self.header)
        if not auth_value:
            raise EmptyToken()
        parts = auth_value.split(" ")

        if parts[0].lower() != self.openapi_scheme:
            if settings.DEBUG:
                logger.error(f"Unexpected auth - '{auth_value}'")
            return None
        token = " ".join(parts[1:])
        return self.authenticate(request, token)

    def authenticate(self, request, token):
        from apps.user.services import UserService
        token = UserService().validate_token(token)
        if token:
            request.user = token.user
            return token
        raise InvalidToken()
