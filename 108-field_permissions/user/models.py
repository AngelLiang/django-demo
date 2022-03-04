from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from field_permissions.models import FieldPermissionModelMixin


class User(FieldPermissionModelMixin, AbstractUser):

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

            # 字段权限
            ('can_change_user_username', _('允许修改帐号的「用户名」字段')),
            ('can_change_user_is_active', _('允许修改帐号的「有效」字段')),
            ('can_change_user_is_staff', _('允许修改帐号的「人员状态」字段')),
        )
