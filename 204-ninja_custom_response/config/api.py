import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        print(response_status, type(data), data)
        return orjson.dumps({
            'code':0,
            'message':'操作成功',
            'data':data
        })

api = NinjaAPI(renderer=ORJSONRenderer())


@api.get("/hello")
def hello(request):
    return {'hello':'world!'}
