from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'import_export',
    'object_import_item',
    'order',
] + INSTALLED_APPS
