import os

from config.django.base import TIME_ZONE

CELERY_TIMEZONE = TIME_ZONE
#
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

CELERY_BROKER_BACKEND = "memory"

# 每个 worker 最多执行3个任务就会被销毁，可防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = int(os.getenv('CELERYD_MAX_TASKS_PER_CHILD', 3))

# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_RESULT_BACKEND = 'django_celery_results.backends.database:DatabaseBackend'

# celery内容等消息的格式设置，默认json
CELERY_ACCEPT_CONTENT = ('application/json', )
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_TASK_DEFAULT_QUEUE = os.getenv('CELERY_TASK_DEFAULT_QUEUE', 'proj')
# CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TASK_DEFAULT_ROUTING_KEY = os.getenv('CELERY_TASK_DEFAULT_ROUTING_KEY', 'proj')

CELERY_TASK_QUEUE_HA_POLICY = 'all'
