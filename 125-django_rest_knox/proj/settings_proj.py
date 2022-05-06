
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'knox',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
}

REST_KNOX = {
    # 每个用户可以发行3个令牌
    'TOKEN_LIMIT_PER_USER': 3,
    'USER_SERIALIZER': None,
    # 每次使用令牌时是否将令牌到期时间延长
    'AUTO_REFRESH': False,
}
