from .settings import *

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'email_sync',
] + INSTALLED_APPS
