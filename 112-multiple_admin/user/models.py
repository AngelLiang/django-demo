from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Meta:
        verbose_name = _('帐号')
        verbose_name_plural = _('帐号')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_user', _('允许添加帐号')),
            ('view_user', _('允许查看帐号')),
            ('change_user', _('允许修改帐号')),
            ('delete_user', _('允许删除帐号')),
            ('import_user', _('允许导入帐号')),
            ('export_user', _('允许导出帐号')),
        )
