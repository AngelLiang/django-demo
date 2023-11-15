from ninja import NinjaAPI
from ninja.errors import ValidationError


class NotFoundError(Exception):
    pass


class ServerError(Exception):

    def __init__(self, message, *args: object) -> None:
        self.message = message
        super().__init__(*args)


def init_error_handler(api: NinjaAPI):
    @api.exception_handler(NotFoundError)
    def handle_not_found_error(request, exc):
        data = {
            'code': 4004,
            'message': 'Not Found',
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
