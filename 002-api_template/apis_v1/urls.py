from django.urls import path
from django.conf.urls import url

from .apis.token import (
    fetch_token_view,
    destory_token_view,
    ping_token_view,
)
from .apis.current_user import (
    current_user_info_view,
)

urlpatterns = [
    # path('apis/v1/token', fetch_token_view),
    path('apis/v1/login', fetch_token_view),
    path('apis/v1/logout', destory_token_view),
    path('apis/v1/ping', ping_token_view),
    path('apis/v1/currentUser', current_user_info_view),

]

# 添加 swagger 文档
from .urls_swagger import urlpatterns as swagger_urls
urlpatterns = urlpatterns + swagger_urls
