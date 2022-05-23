
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 当模型的FileField或ImageField字段有变动或删除模型时，会自动删除旧文件
    'django_cleanup.apps.CleanupConfig',
    'files',
]

import os

from .env import BASE_DIR, env, env_to_enum

from files.enums import FileUploadStrategy, FileUploadStorage


FILE_UPLOAD_STRATEGY = env_to_enum(
    FileUploadStrategy,
    env("FILE_UPLOAD_STRATEGY", default="standard")
)
FILE_UPLOAD_STORAGE = env_to_enum(
    FileUploadStorage,
    env("FILE_UPLOAD_STORAGE", default="local")
)

FILE_MAX_SIZE = env.int("FILE_MAX_SIZE", default=10485760)  # 10 MiB

if FILE_UPLOAD_STORAGE == FileUploadStorage.LOCAL:
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

if FILE_UPLOAD_STORAGE == FileUploadStorage.S3:
    # Using django-storages
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
    AWS_S3_SIGNATURE_VERSION = env("AWS_S3_SIGNATURE_VERSION", default="s3v4")

    # https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl
    AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default="private")

    AWS_PRESIGNED_EXPIRY = env.int("AWS_PRESIGNED_EXPIRY", default=10)  # seconds

APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")
