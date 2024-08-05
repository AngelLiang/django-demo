import datetime

from ninja import NinjaAPI
from ninja.renderers import JSONRenderer
from ninja.responses import NinjaJSONEncoder
# from user.auth import AuthBearer, init_api_auth


class MyJsonEncoder(NinjaJSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(value)


class MyJsonRenderer(JSONRenderer):
    encoder_class = MyJsonEncoder


api = NinjaAPI(
    renderer=MyJsonRenderer(),
)
api.add_router('weixin/', 'weixin_callback.router.router')
# api.add_router('user/', 'user.router.router')
