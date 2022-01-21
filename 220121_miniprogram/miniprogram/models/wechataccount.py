from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class WeChatAccount(models.Model):
    openId = models.CharField(_('OPENID'), max_length=255, default='', blank=False)
    unionId = models.CharField(_('UNIONID'), max_length=255, default='', blank=True)
    session_key = models.CharField(_('SESSION_KEY'), max_length=255, default='', blank=False)

    user = models.OneToOneField(
        User, verbose_name=_('帐号'),
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    userinfo = models.OneToOneField(
        'WeChatUserInfo',
        verbose_name=_('微信个人信息'),
        on_delete=models.CASCADE,
        db_constraint=False,
        null=True, blank=True,
    )

    class Meta:
        verbose_name = _('微信帐号')
        verbose_name_plural = _('微信帐号')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_wechataccount', _('允许添加微信帐号')),
            ('view_wechataccount', _('允许查看微信帐号')),
            ('change_wechataccount', _('允许修改微信帐号')),
            ('delete_wechataccount', _('允许删除微信帐号')),
        )

    def __str__(self):
        if self.userinfo:
            return self.userinfo.nickName
        return self.openId
