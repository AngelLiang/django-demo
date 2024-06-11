from .settings import INSTALLED_APPS

# LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'simpleui',
] + INSTALLED_APPS

SIMPLEUI_HOME_INFO = False
SIMPLEUI_STATIC_OFFLINE = True

SIMPLEUI_CONFIG = {
    'system_keep': False,
    # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    # 'menu_display': ['帐号管理', '定时任务'],
    # 'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
            'app': 'user',
            'name': '帐号管理',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '帐号',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '权限组',
                    'icon': 'fas fa-shield-alt',
                    'url': 'auth/group/'
                }
            ]
        },
        # django_apscheduler
        {
            'app': 'django_apscheduler',
            'name': '定时任务',
            # 'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': 'job executions',
                    # 'icon': 'fa fa-user',
                    'url': 'django_apscheduler/djangojobexecution/'
                },
                {
                    'name': 'jobs',
                    # 'icon': 'fas fa-shield-alt',
                    'url': 'django_apscheduler/djangojob/'
                }
            ]
        },
    ]
}
