import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '初始化基础数据'

    def handle(self, *args, **options):
        pass
