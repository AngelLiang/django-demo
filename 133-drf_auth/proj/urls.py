"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_api.apis.token import (
    fetch_token_view,
    destory_token_view,
    ping_token_view,
)
from auth_api.apis.current_user import current_user_info_view
from auth_api.apis.user_change_password import user_change_password_view
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # path('apis/v1/token', fetch_token_view),
    path('apis/v1/login', fetch_token_view),
    path('apis/v1/logout', destory_token_view),
    path('apis/v1/ping', ping_token_view),
    path('apis/v1/currentUser', current_user_info_view),
    path('apis/v1/changePassword', user_change_password_view),
]

# 添加 swagger 文档
from .urls_swagger import urlpatterns as swagger_urls
urlpatterns = urlpatterns + swagger_urls
