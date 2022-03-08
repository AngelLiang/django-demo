from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'user.apps.UserConfig',
    'product.apps.ProductConfig',
] + INSTALLED_APPS

AUTH_USER_MODEL = 'user.User'
