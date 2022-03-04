from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = INSTALLED_APPS + [
    'user.apps.UserConfig',
]

AUTH_USER_MODEL = 'user.User'
