from ninja import NinjaAPI
from ninja.errors import HttpError
from ninja.errors import ValidationError

from weixin_client.errors import WeiXinClientError
from mox_client.client import MoxClientError

import logging
logger = logging.getLogger('django')


class NotFoundError(Exception):
    def __init__(self, message='资源不存在', *args: object) -> None:
        self.message = message
        super().__init__(*args)


class ServerError(Exception):

    def __init__(self, message, *args: object) -> None:
        self.message = message
        super().__init__(*args)


class InvaildTokenError(HttpError):
    pass


def init_error_handler(api: NinjaAPI):
    @api.exception_handler(NotFoundError)
    def handle_not_found_error(request, exc):
        data = {
            'code': 4004,
            'message': str(exc.message),
            'data': None
        }
        return api.create_response(
            request,
            data,
            status=200,
        )

    @api.exception_handler(ServerError)
    def handle_server_error(request, exc):
        data = {
            'code': 5000,
            'message': 'Server Error',
            'data': {
                'detail': str(exc.message)
            }
        }
        return api.create_response(
            request,
            data,
            status=200,
        )

    @api.exception_handler(ValidationError)
    def handle_validation_error(request, exc):
        data = {
            'code': 4000,
            'message': '校验出错',
            'data': exc.errors
        }
        return api.create_response(
            request,
            data,
            status=200,
        )

    @api.exception_handler(InvaildTokenError)
    def handle_invaild_token_error(request, exc):
        data = {
            'code': 4001,
            'message': str(exc),
            'data': None
        }
        return api.create_response(
            request,
            data,
            status=200,
        )

    @api.exception_handler(WeiXinClientError)
    def handle_weixin_client_error(request, exc: WeiXinClientError):
        logger.exception(exc)
        data = {
            'code': 4000,
            'message': f'请求微信服务错误：{exc}',
            'data': {
                'errcode': exc.errcode,
                'errmsg': exc.errmsg
            }
        }
        return api.create_response(
            request,
            data,
            status=200,
        )

    @api.exception_handler(MoxClientError)
    def handle_mox_client_error(request, exc):
        data = {
            'code': 5000,
            'message': str(exc),
            'data': None
        }
        return api.create_response(
            request,
            data,
            status=200,
        )
