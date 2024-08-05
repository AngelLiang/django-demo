import hashlib
from django.conf import settings
import datetime
from weixin_callback.logger import logger
from weixin_callback.services.ticket import TicketService

WEIXIN_CALLBACK_TOKEN = getattr(settings, 'WEIXIN_CALLBACK_TOKEN')


def generate_sign_url(url):
    # jsapi_ticket = getattr(settings, 'WEIXIN_JSAPI_TICKET')
    jsapi_ticket = TicketService().get_ticket()
    noncestr = 'dashu'
    timestamp = str(int(datetime.datetime.now().timestamp()))
    sign = generate_sign(jsapi_ticket, noncestr, timestamp, url)
    return {
        'noncestr': noncestr,
        # 'jsapi_ticket': jsapi_ticket,
        'timestamp': f'{timestamp}',
        'url': url,
        'sign': sign,
    }


def generate_sign(jsapi_ticket, noncestr, timestamp, url):
    """

    ref: https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign
    """
    data = {
        'noncestr': noncestr,
        'jsapi_ticket': jsapi_ticket,
        'timestamp': f'{timestamp}',
        'url': url,
    }

    # print(data)
    logger.debug(data)
    key_list = sorted(data)
    # print(key_list)
    input_string = ''
    for key in key_list:
        value = data[key]
        if input_string:
            input_string += '&'
        input_string += f'{key}={value}'

    # print(f'input_string:{input_string}')
    value = input_string
    sign = hashlib.sha1(value.encode()).hexdigest()
    return sign


def check_sign(signature: str, timestamp: str, nonce: str) -> int:
    """
    开发者通过检验signature对请求进行校验（下面有校验方式）。若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效，成为开发者成功，否则接入失败。加密/校验流程如下：
    1）将token、timestamp、nonce三个参数进行字典序排序
    2）将三个参数字符串拼接成一个字符串进行sha1加密
    3）开发者获得加密后的字符串可与signature对比，标识该请求来源于微信

    示例
    GET /weixin/?signature=b12542ed6961a6e8bdafda441a80768d37cf5756&echostr=754254657827370935&timestamp=1691997573&nonce=2124542298

    参考资料：https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html
    """
    temp = [WEIXIN_CALLBACK_TOKEN, timestamp, nonce]
    temp_sort = sorted(temp)
    temp_sort_str = ''.join(temp_sort)
    result = hashlib.sha1(temp_sort_str.encode()).hexdigest()
    return signature == result


# def check_sign_by_appid(request, appid: str, signature: str, timestamp: str, nonce: str):
#     from weixin_app.models import WeixinApp
#     from weixin_app.services import WeiXinAppService

#     app: WeixinApp = WeiXinAppService(request).get_by_appid(appid)
#     if not app:
#         return False
#     token = app.token
#     temp_list = [token, timestamp, nonce]
#     temp_sort = sorted(temp_list)
#     temp_sort_str = ''.join(temp_sort)
#     result = hashlib.sha1(temp_sort_str.encode()).hexdigest()
#     return signature == result
