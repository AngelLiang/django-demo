from django.http import FileResponse
from ninja import NinjaAPI

from django.conf import settings

api = NinjaAPI()


@api.get("/donwloadFile")
def upload(request):
    BASE_DIR = settings.BASE_DIR
    filepath = BASE_DIR / 'hello.txt'
    response = FileResponse(open(filepath, "rb"), as_attachment=True)
    return response
