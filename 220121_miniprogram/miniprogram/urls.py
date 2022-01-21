from django.urls import path, include
from .apis.wechatlogin import WeChatLoginAPIView
from .apis.wechatupdateinfo import WeChatUpdateInfoAPIView

urlpatterns = [
    path('login/', WeChatLoginAPIView.as_view(), name='wechat_login'),
    path('updateUserInfo/', WeChatUpdateInfoAPIView.as_view(), name="wechat_update_userinfo"),
]
