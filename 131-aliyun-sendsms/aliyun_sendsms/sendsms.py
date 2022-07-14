import random
import string
import json
import logging

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models

from alibabacloud_tea_openapi.client import TeaException

from django.conf import settings
from django.core.cache import cache as django_cache

ALIYUN_ACCESS_KEY_ID = getattr(settings, 'ALIYUN_ACCESS_KEY_ID', None)
ALIYUN_ACCESS_KEY_SECRET = getattr(settings, 'ALIYUN_ACCESS_KEY_SECRET', None)
ALIYUN_TEMPLATE_CODE = getattr(settings, 'ALIYUN_TEMPLATE_CODE', None)
ALIYUN_SIGN_NAME = getattr(settings, 'ALIYUN_SIGN_NAME', None)


logger = logging.getLogger('aliyun_sendsms')
logger.setLevel(logging.INFO)
log_handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(lineno)d:%(levelname)s:%(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


def generate_random_code(length=6):
    return ''.join(random.sample(string.digits, length))


class SendMsgError(Exception):
    pass


class AliyunSendSms:

    def __init__(self, access_key_id=None, access_key_secret=None, template_code=None,
                 sign_name=None,
                 cache=django_cache,
                 endpoint='dysmsapi.aliyuncs.com'):
        self.access_key_id = access_key_id or ALIYUN_ACCESS_KEY_ID
        self.access_key_secret = access_key_secret or ALIYUN_ACCESS_KEY_SECRET
        self.template_code = template_code or ALIYUN_TEMPLATE_CODE
        self.endpoint = endpoint
        self.sign_name = sign_name or ALIYUN_SIGN_NAME
        self.phone = None
        self.code = None

        self.client = None
        self.send_sms_request = None
        self.cache = cache
        self.timeout = 5 * 60

        self.validate_input_param()
        self.init_client()

    def validate_input_param(self):
        if self.access_key_id is None:
            raise ValueError('access_key_id 参数不能为空')
        if self.access_key_secret is None:
            raise ValueError('access_key_secret 参数不能为空')
        if self.sign_name is None:
            raise ValueError('sign_name 参数不能为空')
        if self.template_code is None:
            raise ValueError('template_code 参数不能为空')

    def init_client(self):
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=self.access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=self.access_key_secret
        )
        # 访问的域名
        config.endpoint = self.endpoint
        self.client = Dysmsapi20170525Client(config)

    def gen_code(self, length=6):
        """生成随机验证码"""
        self.code = ''.join(random.sample(string.digits, length))
        return self.code

    def sendmsg(self, phone, template_param):
        """发送短信

        返回示例

            {'headers': {'date': 'Thu, 14 Jul 2022 06:36:51 GMT', 'content-type': 'application/json;charset=utf-8', 'content-length': '110', 'connection': 'keep-alive', 'access-control-allow-origin': '*', 'access-control-allow-methods': 'POST, GET, OPTIONS, PUT, DELETE', 'access-control-allow-headers': 'X-Requested-With, X-Sequence, _aop_secret, _aop_signature, x-acs-action, x-acs-version, x-acs-date, Content-Type', 'access-control-max-age': '172800', 'x-acs-request-id': 'BEFCDBA8-499D-5A86-B62A-03967E73B4AF', 'x-acs-trace-id': '36eff5a6cd4e3032db9db221db0b4861'}, 
'body': {'BizId': '781720657780611079^0', 'Code': 'OK', 'Message': 'OK', 'RequestId': 'BEFCDBA8-499D-5A86-B62A-03967E73B4AF'}}

        """
        self.send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name=self.sign_name,
            phone_numbers=phone,
            template_code=self.template_code,
            template_param=template_param
        )
        return self.client.send_sms(self.send_sms_request)

    def sendmsg_login_code(self, phone, code):
        """发送登录验证码"""
        template_param = json.dumps({"code": code})
        msg = f'{phone} send {code}'
        logger.info(msg)
        try:
            res = self.sendmsg(phone, template_param)
        except TeaException as e:
            logger.exception(e)
            return False
        return res

    def record_phone(self, phone, code, timeout=None):
        """记录手机号和验证码"""
        if not timeout:
            timeout = self.timeout
        self.cache.set(phone, code, timeout)

    def validate_phone(self, phone, code):
        """校验手机号和验证码"""
        res = self.cache.get(phone)
        return res == code
