import os

from config.django.base import BASE_DIR
from config.env import env

DB_CONFIGS = {
    'sqlite': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mysql': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.mysql'),
        'NAME': env('DB_NAME', default='proj'),
        'USER': env('DB_USER', default='root'),
        'PASSWORD': env('DB_PASS', default='root'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env.int('DB_PORT', default='3306'),
    },
    'pqsql': {
        'ENGINE': env('DB_ENGINE', default='django.db.backends.postgresql_psycopg2'),
        'NAME': env('DB_NAME', default='proj'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASS', default='postgres'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env.int('DB_PORT', default='5432'),
    }
}

DB_TYPE = env('DB_TYPE', default='sqlite')
DATABASES = {
    'default': DB_CONFIGS[DB_TYPE],
}
