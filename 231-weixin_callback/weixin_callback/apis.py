from django.http import HttpResponse
from ninja import Query, Body
from ninja.responses import Response
from weixin_callback.router import router
from weixin_callback.schemas.sign import SignOut, SignIn
from weixin_callback.services.sign import generate_sign, generate_sign_url
from weixin_callback.services.sign import check_sign
from weixin_callback.services.callback import CallBackService
from weixin_callback.services.qrcode import QrcodeService

from utils.response import make_response
from .logger import logger


@router.get("/generate-signature", response=SignOut, summary='生成签名')
def generate_signature(request, url: str, noncestr: str = None, jsapi_ticket: str = None, timestamp: str = None):
    if noncestr is None and jsapi_ticket is None and timestamp is None:
        result = generate_sign_url(url)
    else:
        result = generate_sign(jsapi_ticket, noncestr, timestamp, url)
    return make_response(data=result)


@router.get("/callback", auth=None, operation_id="get_weixin_callback", summary='微信回调接口')
@router.post("/callback", auth=None, operation_id='post_weixin_callback', summary='微信回调接口')
def weixin_callback(request, signature: str, timestamp: str, nonce: str, echostr: int = None, openid: str = None):
    """微信回调接口

    """
    # <xml><ToUserName><![CDATA[gh_f3167383002c]]></ToUserName>\n<FromUserName><![CDATA[oBKHI5sfGeok9WJT8Hqz0Wvw_wZc]]></FromUserName>\n<CreateTime>1692006182</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n<Content><![CDATA[hello]]></Content>\n<MsgId>24223704702442546</MsgId>\n</xml>
    is_check = check_sign(signature, timestamp, nonce)
    if is_check:
        # CallBackService().handle(request.body)
        response_string = CallBackService().handle_scan_qrcode(request)
        if response_string:
            return HttpResponse(response_string)
        return HttpResponse(echostr)
    logger.error('weixin callback check sign error')
    return HttpResponse('')


@router.get("/generate-login-qrcode-image", summary='生成登录二维码图片')
def get_login_qrcode_image(request, ticket: str = None):
    response_content = QrcodeService().get_login_qrcode_image(ticket=ticket)
    http_response = HttpResponse(
        response_content,
        content_type='image/jpeg'  # 根据实际情况更改MIME类型
    )
    return http_response


@router.get("/generate-login-qrcode", summary='生成登录二维码')
def generate_login_qrcode(request):
    data = QrcodeService().create_login_qrcode()
    return make_response(data=data)


@router.get("/monitor-login-qrcode", response={400: dict, 200: dict}, summary='监听登录二维码')
def monitor_login_qrcode(request, ticket: str):
    token = QrcodeService().get_ticket_token(ticket)
    if not token:
        return make_response(code=400)
    return make_response(data={'token': token})
