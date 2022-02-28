import os

MINIPROGRAM_CONFIG = {
    "APPID": os.getenv('MINIPROGRAM_APPID', ''),
    "SECRET": os.getenv('MINIPROGRAM_SECRET', ''),
    "WECHAT_PAY": {
        "MCH_ID": "",  # 微信支付商户号
        "KEY": "",  # API密钥
        "NOTIFICATION_URL": '',  # 微信支付回调地址
    },
}
