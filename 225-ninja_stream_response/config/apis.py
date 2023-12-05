from ninja import NinjaAPI
from django.http import StreamingHttpResponse

api = NinjaAPI()


def stream(number=10):
    for data in range(number):
        yield str({'data': data}) + '\r\n'


@api.get('/stream')
def get_stream(request):
    return StreamingHttpResponse(stream())
