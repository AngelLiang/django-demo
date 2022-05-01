## 安装

    pip install django-dbbackup

## 配置

settings.py

    INSTALLED_APPS = (
        ...
        'dbbackup',  # django-dbbackup
    )

    DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
    DBBACKUP_STORAGE_OPTIONS = {'location': '/my/backup/dir/'}
