from ninja import NinjaAPI, Router

router = Router(tags=['微信相关'])

from weixin_callback.apis import *  # noqa


def init_weixin_router(api: NinjaAPI):

    # @api.exception_handler(UserServiceError)
    # def handle_user_service_error(request, exc):
    #     return api.create_response(
    #         request,
    #         {
    #             'code': 400,
    #             'message': str(exc),
    #             'data': {}
    #         },
    #         status=200,
    #     )

    api.add_router('weixin/', router)
