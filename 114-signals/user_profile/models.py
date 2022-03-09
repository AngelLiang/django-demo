from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='用户',
        on_delete=models.CASCADE,
        db_constraint=False,
    )
    name = models.CharField('名称', max_length=255)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_userprofile', _('允许添加用户信息')),
            ('view_userprofile', _('允许查看用户信息')),
            ('change_userprofile', _('允许修改用户信息')),
            ('delete_userprofile', _('允许删除用户信息')),
        )

    def __str__(self):
        return f'{self.name}'


from .signals import *
