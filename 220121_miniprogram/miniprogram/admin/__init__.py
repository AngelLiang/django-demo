from django.contrib import admin
from .wechataccount import WeChatAccountAdmin
from .wechatuserinfo import WeChatUserInfoAdmin
# from .wechatphone import WeChatPhoneAdmin

from .. import models

admin.site.register(models.WeChatAccount, WeChatAccountAdmin)
admin.site.register(models.WeChatUserInfo, WeChatUserInfoAdmin)
# admin.site.register(models.WeChatPhone, WeChatPhoneAdmin)
