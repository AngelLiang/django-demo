
import os
from .settings import BASE_DIR

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

LOGS_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_PATH):
    os.mkdir(LOGS_PATH)

LOGGING = {
    'version': 1,
    # 禁用已经存在的logger实例
    'disable_existing_loggers': True,
    # 日志文件的格式
    'formatters': {
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 'null': {
        #     'level': 'DEBUG',
        #     'class': 'django.utils.log.NullHandler',
        # },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        'default': {    # 默认的
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_DIR, 'logs', "all.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,                    # 日志大小 50M
            'backupCount': 3,                                # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {   # 专门用来记错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_DIR, 'logs', "error.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'collect': {   # 专门定义一个收集特定信息的日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_DIR, 'logs', "collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', "script.log"),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },
    'loggers': {
        # 默认的 logger 应用如下配置
        'django': {
            # 上线之后可以把 'console' 移除
            'handlers': ['default', 'console', 'error'],
            'level': 'ERROR',
            'propagate': True,  # 是否向更高级别的logger传递
        },
        # 记录与请求处理相关的消息
        # 5XX 为 ERROR
        # 4XX 为 WARNING
        # example: [WARNING][2022-05-05 09:32:00,676][log.py:228]Not Found: /404
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        # 请求执行的每个应用程序级别的 SQL 语句都会在该DEBUG级别记录到此记录器。
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'MYAPP': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        # },
    }
}
