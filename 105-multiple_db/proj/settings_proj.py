import os

from .settings import BASE_DIR
from .settings import INSTALLED_APPS

INSTALLED_APPS = INSTALLED_APPS + [
    'product.apps.ProductConfig',
    'order.apps.OrderConfig',
]

DATABASES = {
    'default': {
    },
    # 认证数据库
    'auth_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'auth.sqlite3'),
    },
    # 主数据库
    'primary': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'primary.sqlite3'),
    },
    # 订单数据库
    'order_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'order.sqlite3'),
    },
}

DATABASE_ROUTERS = [
    'proj.router.AuthRouter',
    'proj.router.OrderRouter',
    'proj.router.PrimaryReplicaRouter'
]
