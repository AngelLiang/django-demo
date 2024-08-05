from django.core.cache import cache
from django.conf import settings
from ninja.errors import HttpError
from weixin_callback.logger import logger
from weixin_callback.services.token import TokenService
from clients.weixin_client.client import WeiXinClient

TICKET_KEY = 'weixin_ticket'


class TicketServiceError(Exception):
    pass


class TicketService:
    def __init__(self) -> None:
        self.client: WeiXinClient = WeiXinClient()

        self.appid = getattr(settings, 'WEIXIN_APPID')
        self.appsecret = getattr(settings, 'WEIXIN_APPSECRET')
        if not self.appid:
            raise TicketServiceError('appid不能为空')
        if not self.appsecret:
            raise TicketServiceError('appsecret不能为空')

    def request_ticket(self):
        logger.debug('请求微信的ticket')
        token = TokenService().get_token()
        resp_json = self.client.get_jsapi_ticket(token)
        if resp_json['errcode'] == 0:
            return resp_json['ticket']
        else:
            pass

    def cache_ticket(self, ticket, timeout=7200):
        logger.debug('缓存微信的ticket')
        return cache.set(TICKET_KEY, ticket, timeout)

    def get_ticket_from_cache(self):
        logger.debug('从缓存获取微信的ticket')
        return cache.get(TICKET_KEY)

    def get_ticket(self):
        """获取ticket"""
        ticket = self.get_ticket_from_cache()
        if not ticket:
            ticket = self.request_ticket()
            self.cache_ticket(ticket)
        return ticket
