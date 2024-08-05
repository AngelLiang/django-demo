from .result_code import *


class WeiXinClientError(Exception):
    def __init__(self, errcode=0, errmsg='', *args, **kwargs):
        self.errcode = errcode
        self.errmsg = errmsg
