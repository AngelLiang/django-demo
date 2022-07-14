import os

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aliyun_sendsms',
]

ALIYUN_ACCESS_KEY_ID = os.getenv('ALIYUN_ACCESS_KEY_ID')
ALIYUN_ACCESS_KEY_SECRET = os.getenv('ALIYUN_ACCESS_KEY_SECRET')
ALIYUN_SIGN_NAME = os.getenv('ALIYUN_SIGN_NAME')
ALIYUN_TEMPLATE_CODE = os.getenv('ALIYUN_TEMPLATE_CODE')
ALIYUN_TEST_PHONE = os.getenv('ALIYUN_TEST_PHONE')
