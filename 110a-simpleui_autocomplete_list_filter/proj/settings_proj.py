
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 添加下面的app
    'dal',
    'dal_select2',
    'admin_auto_filters',

    'user',
    'app',
]

SIMPLEUI_HOME_INFO = False
