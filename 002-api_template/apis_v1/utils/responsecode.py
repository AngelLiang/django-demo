from rest_framework.response import Response


class ResponseCodeBase(type):
    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)
        if not hasattr(cls, 'registory'):
            # this is the base class
            cls.registory = {}
        else:
            # this is the subclass
            # cls.registory[name.lower()] = cls
            cls.registory[cls.code] = cls


class ResponseCode(object, metaclass=ResponseCodeBase):
    code = None
    devmsg = None
    usermsg = None

    @classmethod
    def handle(cls, code):
        return cls.registory.get(code, None)

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
        })
        return response


class SuccessResponse(ResponseCode):
    code = 2000
    devmsg = None
    usermsg = None

    @classmethod
    def get_response(cls, request, data=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'data': data or {}
        })
        return response


class FailResponse(ResponseCode):
    code = 4000
    devmsg = '请求错误'
    usermsg = '请求错误'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
            'errors': errors or {}
        })
        return response


class ValidationError(ResponseCode):
    code = 4000
    devmsg = '请求数据校验错误'
    usermsg = '请求数据校验错误'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
            'errors': errors or {}
        })
        return response


class NotAuthenticatedError(ResponseCode):
    code = 4002
    devmsg = '没有认证'
    usermsg = '没有认证'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
        })
        return response


class AuthenticationFailedError(ResponseCode):
    code = 4003
    devmsg = '认证失败'
    usermsg = '认证失败'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
        })
        return response


class NotFoundError(ResponseCode):
    code = 4004
    devmsg = '找不到信息'
    usermsg = '找不到信息'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
        })
        return response


class ThrottledError(ResponseCode):
    code = 4005
    devmsg = '请求太快了'
    usermsg = '请求太快了'

    @classmethod
    def get_response(cls, request, devmsg=None, usermsg=None, errors=None):
        response = Response({
            'code': cls.code,
            'self': request.get_full_path(),
            'devMsg': devmsg or cls.devmsg,
            'userMsg': usermsg or cls.usermsg,
        })
        return response


class UserNotFound(ResponseCode):
    code = 1001
    devmsg = '没有该用户'
    usermsg = '没有该用户'


class PasswordError(ResponseCode):
    code = 1002
    devmsg = '密码错误'
    usermsg = '密码错误'


class UserNoBindError(ResponseCode):
    code = 1003
    devmsg = '没有绑定用户'
    usermsg = '没有绑定用户'


class UserAlreadyBindError(ResponseCode):
    code = 1004
    devmsg = '已经绑定用户'
    usermsg = '已经绑定用户'


class ServerError(ResponseCode):
    code = 5000
    devmsg = '服务端错误'
    usermsg = '服务端错误'
