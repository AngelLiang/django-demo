"""
Usage::

    # settings.py
    INSTALLED_APPS = [
        # 'django.contrib.admin',  # 替换这一句
        'proj.adminsite.AdminConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

"""
from django.contrib import admin
from django.contrib.admin.apps import AdminConfig as _AdminConfig


name = '后台管理系统'


class AdminSite(admin.AdminSite):
    site_header = name
    site_title = name
    index_title = name


class AdminConfig(_AdminConfig):
    default_site = 'proj.adminsite.AdminSite'
