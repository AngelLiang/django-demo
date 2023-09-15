from ninja import NinjaAPI
from ninja.security import APIKeyQuery
from ninja.security import APIKeyHeader


api = NinjaAPI()


class InvalidToken(Exception):
    pass

@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(request, {"code": 4001, 'message':'Invalid token', 'data': None}, status=401)

class HeaderKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        if key == "supersecret":
            return key
        raise InvalidToken()


header_key = HeaderKey()


@api.get("/headerkey", auth=header_key)
def apikey(request):
    return f"Token = {request.auth}"


class QueryKey(APIKeyQuery):
    param_name = "api_key"

    def authenticate(self, request, key):
        if key == "token":
            return key
        raise InvalidToken()


query_key = QueryKey()


@api.get("/multiple", auth=[query_key, header_key])
def multiple(request):
    return f"Token = {request.auth}"

# @api.get("/apikey", auth=api_key)
# def apikey(request):
#     return f"Hello {request.auth}"
