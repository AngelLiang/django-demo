from django.urls import path, include
from django.conf.urls import url

from .auth_api import UserLoginApi


urlpatterns = [
    path('login', UserLoginApi.as_view())
]
