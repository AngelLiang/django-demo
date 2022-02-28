from django.urls import path
from django.conf.urls import url

from .apis import AppTokenPingAPIView


urlpatterns = [
    path('apptoken/ping', AppTokenPingAPIView.as_view()),
]

# 添加 swagger 文档
from .urls_swagger import urlpatterns as swagger_urls
urlpatterns = urlpatterns + swagger_urls

