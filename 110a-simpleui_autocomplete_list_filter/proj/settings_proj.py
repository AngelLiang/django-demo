
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    # 添加下面的app
    'dal',
    'dal_select2',
    'autocomplete_light_utils',
    'admin_auto_filters',
    'admin_auto_filters_utils',

    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'user',
    'app',
]

SIMPLEUI_HOME_INFO = False
