from cProfile import label
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class Department(models.Model):
    name = models.CharField('部门名称', max_length=255)
    user = models.ForeignKey(
        User,
        verbose_name='负责人',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        db_constraint=False,
    )

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_department', _('允许添加部门')),
            ('view_department', _('允许查看部门')),
            ('change_department', _('允许修改部门')),
            ('delete_department', _('允许删除部门')),
        )

    def __str__(self):
        return f'{self.name}'
