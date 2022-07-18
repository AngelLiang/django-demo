import datetime

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
    # add
    'knox',
]

REST_FRAMEWORK = {
    # add
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',),
}

# add
REST_KNOX = {
    # 发送给客户端的令牌的长度
    # 'AUTH_TOKEN_CHARACTER_LENGTH': 64,

    # 令牌在过期之前可以存在的时间。过期的令牌会自动从系统中删除。
    # 'TOKEN_TTL': datetime.timedelta(hours=10),

    # 控制每个用户可以发行多少令牌
    # 'TOKEN_LIMIT_PER_USER': None,


    'USER_SERIALIZER': None,

    # 每次使用令牌时是否将令牌到期时间延长
    'AUTO_REFRESH': False,

    # 在数据库中更新令牌到期所需经过的最短时间（以秒为单位）
    # 'MIN_REFRESH_INTERVAL': 60 * 5,
    # Token 前缀
    'AUTH_HEADER_PREFIX': 'Token',
}
