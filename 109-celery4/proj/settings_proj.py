from .settings import INSTALLED_APPS

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = INSTALLED_APPS + [
    'django_celery_beat',
    'django_celery_results',
    'task.apps.TaskConfig',
]
