
import os
from .settings import BASE_DIR

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'


# LOG_PATH = env('LOG_PATH', default=os.path.join(BASE_DIR, 'log'))
LOG_PATH = os.path.join(BASE_DIR, 'log')
os.makedirs(LOG_PATH, exist_ok=True)


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 简单的日志格式
        'simple': {
            # 'format': f'%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d - %(message)s'
            'format': f'{Bcolors.OKGREEN}%(asctime)s{Bcolors.ENDC} | %(levelname)s | {Bcolors.OKBLUE}%(filename)s:%(lineno)d{Bcolors.ENDC} - %(message)s'
        },
        # 访问日志格式
        'standard': {
            'format': '%(asctime)s | %(levelname)s | %(message)s'
        },
        # 详细的日志格式
        'detail': {
            'format': '%(asctime)s | %(levelname)s | %(threadName)s:%(thread)d | task_id:%(name)s | %(filename)s:%(lineno)d | %(message)s'

        },
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        'console': {     # 在终端打印
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        'default': {    # 默认的
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(LOG_PATH, "all.log"),  # 日志文件
            # 日志文件生成规律：当前记录的文件是原文件名，过了时间后，会把过去时间文件名加上时间后缀，进行归档
            # 例子
            'when': 'D',  # 'S' 'M' 'H' 'D' 'W0'-'W6' 'midnight'
            'backupCount': 180,                                # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {   # 专门用来记错误日志
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(LOG_PATH, "error.log"),  # 日志文件
            # 日志文件生成规律：当前记录的文件是原文件名，过了时间后，会把过去时间文件名加上时间后缀，进行归档
            # 例子
            'when': 'D',  # 'S' 'M' 'H' 'D' 'W0'-'W6' 'midnight'
            'backupCount': 180,                                # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(LOG_PATH, "script.log"),  # 日志文件
            # 日志文件生成规律：当前记录的文件是原文件名，过了时间后，会把过去时间文件名加上时间后缀，进行归档
            # 例子
            'when': 'D',  # 'S' 'M' 'H' 'D' 'W0'-'W6' 'midnight'
            'backupCount': 180,                                # 最多备份几个
            'formatter': 'standard',
        },
        'access_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(LOG_PATH, "access.log"),  # 日志文件
            # 日志文件生成规律：当前记录的文件是原文件名，过了时间后，会把过去时间文件名加上时间后缀，进行归档
            # 例子
            'when': 'D',  # 'S' 'M' 'H' 'D' 'W0'-'W6' 'midnight'
            'backupCount': 180,                                # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(LOG_PATH, "request.log"),  # 日志文件
            # 日志文件生成规律：当前记录的文件是原文件名，过了时间后，会把过去时间文件名加上时间后缀，进行归档
            # 例子
            'when': 'D',  # 'S' 'M' 'H' 'D' 'W0'-'W6' 'midnight'
            'backupCount': 180,                                # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        }
    },
    'loggers': {
        'django': {             # 默认的 logger 应用如下配置
            'handlers': ['default', 'error'],  # 上线之后可以把 'console' 移除
            'level': 'ERROR',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        'django.server': {
            'handlers': ['console', 'access_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'request_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        },
        # 'scripts': {
        #     'handlers': ['scprits_handler'],
        #     'level': 'ERROR',
        #     'propagate': False
        # },
    },
}
