from ninja import NinjaAPI
from .schemas import LoginSchema, TokenSchema
from .services import LoginService

api = NinjaAPI()


@api.post("/login", response=TokenSchema)
def login(request, params: LoginSchema):
    token = LoginService().login(request,**params.dict())
    return {
        'token': token
    }
