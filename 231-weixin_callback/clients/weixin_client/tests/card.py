import os
import sys
from dotenv import load_dotenv

sys.path.append(os.getcwd())

env_path = os.path.join(os.getcwd(), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

WEIXIN_APPID = os.getenv('WEIXIN_APPID')
WEIXIN_APPSECRET = os.getenv('WEIXIN_APPSECRET')
if not WEIXIN_APPID:
    raise ValueError('appid错误')
if not WEIXIN_APPSECRET:
    raise ValueError('appsecret错误')


def test_add_groupon():
    """添加卡券"""
    from weixin_client.client import WeiXinClient
    client = WeiXinClient()
    json_resp = client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    # json_resp = client.get_access_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    print(f'json_resp:{json_resp}')
    assert 'access_token' in json_resp
    token = json_resp['access_token']

    data = {
        "card": {
            # GROUPON: 团购券
            # CASH: 代金券
            # DISCOUNT: 折扣券
            # GIFT: 兑换券
            # GENERAL_COUPON: 优惠券
            "card_type": "GROUPON",

            # 替换类型的话，这里也要替换
            "groupon": {
                "base_info": {
                    # 必填。卡券的商户logo，建议像素为300*300。
                    "logo_url": "http://mmbiz.qpic.cn/mmbiz_jpg/qkWSj3kc7DmhsDH2kaqhCteAN8eKPzZiaTibKaAXX4AibkvHhZngDwGndqjcbX5E7wPyQr1jYy46F2q4fh8c9xhYA/0",

                    # 必填。商户名字,字数上限为12个汉字。
                    "brand_name": "微信餐厅",

                    # 必填。码型：
                    # "CODE_TYPE_TEXT"文 本 ；
                    # "CODE_TYPE_BARCODE"一维码
                    # "CODE_TYPE_QRCODE"二维码
                    # "CODE_TYPE_ONLY_QRCODE",二维码无code显示；
                    # "CODE_TYPE_ONLY_BARCODE",一维码无code显示
                    # CODE_TYPE_NONE， 不显示code和条形码类型
                    "code_type": "CODE_TYPE_TEXT",

                    # 必填。卡券名，字数上限为9个汉字。(建议涵盖卡券属性、服务及金额)。
                    "title": "132元双人火锅套餐",
                    # "sub_title": "周末狂欢必备",

                    # 必填。券颜色。按色彩规范标注填写Color010-Color100。
                    "color": "Color010",

                    # 必填。卡券使用提醒，字数上限为16个汉字。
                    "notice": "使用时向服务员出示此券",

                    # 必填。卡券使用说明，字数上限为1024个汉字。
                    "description": "不可与其他优惠同享",
                    # 必填。使用日期，有效期的信息。
                    "date_info": {
                        # 必填。使用时间的类型，旧文档采用的1和2依然生效。
                        "type": "DATE_TYPE_FIX_TERM",
                        # 必填。type为DATE_TYPE_FIX_TERM时专用，表示自领取后多少天内有效，不支持填写0。
                        "fixed_term": 15,
                        # 必填。type为DATE_TYPE_FIX_TERM时专用，表示自领取后多少天开始生效，领取后当天生效填写0。（单位为天）
                        "fixed_begin_term": 0
                    },
                    # 必填。商品信息。
                    "sku": {
                        # 必填。卡券库存的数量，上限为100000000。
                        "quantity": 10
                    },

                    "service_phone": "020-88888888",
                    # 每人可领券的数量限制,不填写默认为50。
                    "get_limit": 3,
                    # 需自定义Code码的商家必须在创建卡券时候，设定use_custom_code为true
                    "use_custom_code": False,
                    # 是否指定用户领取，填写true或false 。默认为false。通常指定特殊用户群体 投放卡券或防止刷券时选择指定用户领取。
                    "bind_openid": False,
                    # can_share字段指领取卡券原生页面是否可分享，建议指定Code码、指定OpenID等强限制条件的卡券填写false。
                    "can_share": True,
                    "can_give_friend": True,

                    # 门店位置poiid。 调用 POI门店管理接 口 获取门店位置poiid。具备线下门店 的商户为必填。
                    # 请点击查看微信门店接口文档，获取门店 ID 后填入创建卡券接口中的相应字段 location_id_list，即可设置该卡券的适用门店。
                    "location_id_list": [],
                    # "custom_url_name": "立即使用",
                    # "custom_url": "http://www.qq.com",

                    # 卡券跳转的小程序的user_name，仅可跳转该 公众号绑定的小程序 。
                    # "custom_app_brand_user_name": "gh_86a091e50ad4@app",
                    # "custom_url_sub_title": "更多惊喜",
                    # "promotion_url_name": "更多优惠",
                    # "promotion_url": "http://www.qq.com",
                    # "promotion_app_brand_user_name": "gh_86a091e50ad4@app",
                    # "promotion_app_brand_pass": "API/cardPage"
                },
                "deal_detail": "deal_detail"
            }
        }
    }

    resp_json = client.add_card(token, json=data)
    print(resp_json)
    assert resp_json['errcode'] == 0


def test_add_general_coupon():
    """添加优惠券"""
    from weixin_client.client import WeiXinClient
    from weixin_client.client import WeiXinClient
    client = WeiXinClient()
    json_resp = client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    # json_resp = client.get_access_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    print(f'json_resp:{json_resp}')
    assert 'access_token' in json_resp
    token = json_resp['access_token']

    data = {
        "card": {
            # GROUPON: 团购券
            # CASH: 代金券
            # DISCOUNT: 折扣券
            # GIFT: 兑换券
            # GENERAL_COUPON: 优惠券
            "card_type": "GENERAL_COUPON",

            # 替换类型的话，这里也要替换
            "general_coupon": {
                "base_info": {
                    # 必填。卡券的商户logo，建议像素为300*300。
                    "logo_url": "http://mmbiz.qpic.cn/mmbiz_jpg/qkWSj3kc7DmhsDH2kaqhCteAN8eKPzZiaTibKaAXX4AibkvHhZngDwGndqjcbX5E7wPyQr1jYy46F2q4fh8c9xhYA/0",

                    # 必填。商户名字,字数上限为12个汉字。
                    "brand_name": "微信餐厅",

                    # 必填。码型：
                    # "CODE_TYPE_TEXT"文 本 ；
                    # "CODE_TYPE_BARCODE"一维码
                    # "CODE_TYPE_QRCODE"二维码
                    # "CODE_TYPE_ONLY_QRCODE",二维码无code显示；
                    # "CODE_TYPE_ONLY_BARCODE",一维码无code显示
                    # CODE_TYPE_NONE， 不显示code和条形码类型
                    "code_type": "CODE_TYPE_TEXT",

                    # 必填。卡券名，字数上限为9个汉字。(建议涵盖卡券属性、服务及金额)。
                    "title": "132元双人火锅套餐",
                    # "sub_title": "周末狂欢必备",

                    # 必填。券颜色。按色彩规范标注填写Color010-Color100。
                    "color": "Color010",

                    # 必填。卡券使用提醒，字数上限为16个汉字。
                    "notice": "使用时向服务员出示此券",

                    # 必填。卡券使用说明，字数上限为1024个汉字。
                    "description": "不可与其他优惠同享",
                    # 必填。使用日期，有效期的信息。
                    "date_info": {
                        # 必填。使用时间的类型，旧文档采用的1和2依然生效。
                        "type": "DATE_TYPE_FIX_TERM",
                        # 必填。type为DATE_TYPE_FIX_TERM时专用，表示自领取后多少天内有效，不支持填写0。
                        "fixed_term": 15,
                        # 必填。type为DATE_TYPE_FIX_TERM时专用，表示自领取后多少天开始生效，领取后当天生效填写0。（单位为天）
                        "fixed_begin_term": 0
                    },
                    # 必填。商品信息。
                    "sku": {
                        # 必填。卡券库存的数量，上限为100000000。
                        "quantity": 10
                    },

                    "service_phone": "020-88888888",
                    # 每人可领券的数量限制,不填写默认为50。
                    "get_limit": 3,
                    # 需自定义Code码的商家必须在创建卡券时候，设定use_custom_code为true
                    "use_custom_code": False,
                    # 是否指定用户领取，填写true或false 。默认为false。通常指定特殊用户群体 投放卡券或防止刷券时选择指定用户领取。
                    "bind_openid": False,
                    # can_share字段指领取卡券原生页面是否可分享，建议指定Code码、指定OpenID等强限制条件的卡券填写false。
                    "can_share": True,
                    "can_give_friend": True,

                    # 门店位置poiid。 调用 POI门店管理接 口 获取门店位置poiid。具备线下门店 的商户为必填。
                    # 请点击查看微信门店接口文档，获取门店 ID 后填入创建卡券接口中的相应字段 location_id_list，即可设置该卡券的适用门店。
                    "location_id_list": [],
                    # "custom_url_name": "立即使用",
                    # "custom_url": "http://www.qq.com",

                    # 卡券跳转的小程序的user_name，仅可跳转该 公众号绑定的小程序 。
                    # "custom_app_brand_user_name": "gh_86a091e50ad4@app",
                    # "custom_url_sub_title": "更多惊喜",
                    # "promotion_url_name": "更多优惠",
                    # "promotion_url": "http://www.qq.com",
                    # "promotion_app_brand_user_name": "gh_86a091e50ad4@app",
                    # "promotion_app_brand_pass": "API/cardPage"
                },
                "default_detail": "优惠券专用，填写优惠详情"
            }
        }
    }

    resp_json = client.add_card(token, json=data)
    print(resp_json)
    assert resp_json['errcode'] == 0


def test_batchget_card():
    """批量查询卡券列表"""
    from weixin_client.client import WeiXinClient
    client = WeiXinClient()
    json_resp = client.get_stable_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    # json_resp = client.get_access_token(WEIXIN_APPID, WEIXIN_APPSECRET)
    print(f'json_resp:{json_resp}')
    assert 'access_token' in json_resp
    token = json_resp['access_token']

    resp_json = client.batchget_card(token)
    print(resp_json)
    assert resp_json['errcode'] == 0


if __name__ == '__main__':
    test_add_general_coupon()
