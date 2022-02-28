# miniprogram_api/admin/wechataccount.py
from django.contrib import admin


class WeChatAccountAdmin(admin.ModelAdmin):
    list_display = ('openId', 'unionId', 'userinfo')
