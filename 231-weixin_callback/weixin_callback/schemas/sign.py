from ninja import Schema


class SignIn(Schema):
    url: str
    noncestr: str = None
    jsapi_ticket: str = None
    timestamp: str = None


class SignData(Schema):
    url: str
    noncestr: str = None
    sign: str = None
    timestamp: str = None


class SignOut(Schema):
    code: int = 0
    message: str = 'success'
    data: SignData
