from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = INSTALLED_APPS + [
    'import_export',
    'django_tables2',
    'river',
    'river_utils',
    'ticket.apps.TicketConfig',
]

