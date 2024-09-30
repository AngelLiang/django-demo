from django.core.cache import cache
from django.conf import settings
from ninja.errors import HttpError
from weixin_callback.logger import logger
from weixin_callback.services.token import TokenService
from clients.weixin_client.client import WeiXinClient


TICKET_CACEH_KEY = 'ticket'
# 场景值
LOGIN_SCENE_ID = 1


class QrcodeServiceError(Exception):
    pass


class QrcodeService:
    def __init__(self):
        self.client: WeiXinClient = WeiXinClient()
        self.appid = getattr(settings, 'WEIXIN_APPID')
        self.appsecret = getattr(settings, 'WEIXIN_APPSECRET')
        if not self.appid:
            raise QrcodeServiceError('appid不能为空')
        if not self.appsecret:
            raise QrcodeServiceError('appsecret不能为空')

    def create_login_qrcode(self) -> dict:
        token = TokenService().get_stable_token()
        qrcode = self.client.create_temp_qrcode(token, LOGIN_SCENE_ID)
        logger.debug(qrcode)
        # {"ticket":"gQH47joAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL2taZ2Z3TVRtNzJXV1Brb3ZhYmJJAAIEZ23sUwMEmm3sUw==","expire_seconds":60,"url":"http://weixin.qq.com/q/kZgfwMTm72WWPkovabbI"}
        result = {
            'ticket': qrcode['ticket'],
            'expire_seconds': qrcode['expire_seconds'],
            'url': qrcode['url'],
            'qrcode': f'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket={qrcode["ticket"]}'
        }
        return result

    def get_temp_qrcode_by_ticket(self, ticket: str):
        resp = self.client.get_qrcode_image(ticket)
        response_content = resp.content
        return response_content

    def get_login_qrcode_image(self, ticket: str = None):
        if not ticket:
            qrcode = self.create_login_qrcode()
            ticket = qrcode['ticket']
        resp = self.client.get_qrcode_image(ticket)
        return resp.content

    def set_ticket_token(self, ticket: str, token: str):
        cache.set(f'{TICKET_CACEH_KEY}:{ticket}', token, 60 * 3)

    def get_ticket_token(self, ticket: str):
        return cache.get(f'{TICKET_CACEH_KEY}:{ticket}', None)
