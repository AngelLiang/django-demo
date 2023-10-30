import datetime
from django.utils.timezone import localtime

from ninja import NinjaAPI
from ninja.renderers import JSONRenderer
from ninja.responses import NinjaJSONEncoder

from user.apis import router as user_router


class MyJsonEncoder(NinjaJSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(value)


class MyJsonRenderer(JSONRenderer):
    encoder_class = MyJsonEncoder


api = NinjaAPI(renderer=MyJsonRenderer())

api.add_router("/user/", user_router)
