import datetime
from django.utils import timezone


def get_now():
    return datetime.datetime.now()


def get_django_now():
    return timezone.now()
