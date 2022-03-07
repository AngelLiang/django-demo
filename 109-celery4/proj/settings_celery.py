import platform
import os

from .settings import TIME_ZONE

# Windows 平台需要设置 FORKED_BY_MULTIPROCESSING 变量，否则可能报错
if platform.system() == 'Windows':
    os.environ['FORKED_BY_MULTIPROCESSING'] = '1'

# CELERY
CELERY_BROKER_URL = 'amqp://guest:guest@127.0.0.1:5672/'
CELERY_TIMEZONE = TIME_ZONE

# CELERY_TASK_DEFAULT_QUEUE = 'django'
# CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
# CELERY_task_default_routing_key = 'django'

# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'

# CELERY_RESULT_BACKEND = 'django_celery_results.backends.database:DatabaseBackend'
# # celery内容等消息的格式设置，默认json
# CELERY_ACCEPT_CONTENT = ('application/json', )
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
