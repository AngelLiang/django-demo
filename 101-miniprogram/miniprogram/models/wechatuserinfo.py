"""
https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/UserInfo.html
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class WeChatUserInfo(models.Model):
    nickName = models.CharField(_('微信昵称'), max_length=100, default='', blank=False)
    avatarUrl = models.CharField(_('微信头像'), max_length=255, null=True, blank=False)

    GENDER_CHOICES = [
        (0, _('未知')),
        (1, _('男性')),
        (2, _('女性')),
    ]
    gender = models.CharField(_('性别'), max_length=2, null=True, blank=False, choices=GENDER_CHOICES)
    city = models.CharField(_('城市'), max_length=100, default='', blank=False)
    province = models.CharField(_('省份'), max_length=100, default='', blank=False)
    country = models.CharField(_('国家'), max_length=100, default='', blank=False)

    class Meta:
        verbose_name = _('微信个人信息')
        verbose_name_plural = _('微信个人信息')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_wechatuserinfo', _('允许添加微信个人信息')),
            ('view_wechatuserinfo', _('允许查看微信个人信息')),
            ('change_wechatuserinfo', _('允许修改微信个人信息')),
            ('delete_wechatuserinfo', _('允许删除微信个人信息')),
        )

    def __str__(self):
        return self.nickName
