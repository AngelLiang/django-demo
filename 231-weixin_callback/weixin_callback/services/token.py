from django.core.cache import cache
from django.conf import settings
from clients.weixin_client.client import WeiXinClient
from weixin_callback.logger import logger

TOKEN_KEY = 'weixin_token:{appid}'


class TokenServiceError(Exception):
    pass


class TokenService:
    def __init__(self, appid=None, appsecret=None) -> None:
        self.client: WeiXinClient = WeiXinClient()
        self.appid = appid or getattr(settings, 'WEIXIN_APPID')
        self.appsecret = appsecret or getattr(settings, 'WEIXIN_APPSECRET')

    def request_token(self):
        logger.debug(f'请求微信appid={self.appid}的token')
        resp_json = self.client.get_access_token(appid=self.appid, appsecret=self.appsecret)
        # logger.debug(resp_json)
        if 'errcode' in resp_json and resp_json['errcode'] != 0:
            raise TokenServiceError(message=resp_json['errmsg'])
        access_token = resp_json['access_token']
        return access_token

    def request_stable_token(self, force_refresh=False):
        logger.debug(f'请求微信appid={self.appid}的stable_token')
        resp_json = self.client.get_stable_token(
            appid=self.appid, appsecret=self.appsecret, force_refresh=force_refresh)
        if 'errcode' in resp_json and resp_json['errcode'] != 0:
            raise TokenServiceError(message=resp_json['errmsg'])
        access_token = resp_json['access_token']
        return access_token

    def set_token_cache(self, token, timeout=7200):
        logger.debug(f'缓存微信appid={self.appid}的token')
        key = TOKEN_KEY.format(appid=self.appid)
        return cache.set(key, token, timeout)

    def get_token_from_cache(self):
        logger.debug(f'从缓存获取微信appid={self.appid}的token')
        key = TOKEN_KEY.format(appid=self.appid)
        return cache.get(key)

    def get_token(self):
        token = self.get_token_from_cache()
        if not token:
            token = self.request_token()
            self.set_token_cache(token)
        return token

    def get_stable_token(self):
        token = self.get_token_from_cache()
        if not token:
            token = self.request_stable_token()
            self.set_token_cache(token)
        return token
