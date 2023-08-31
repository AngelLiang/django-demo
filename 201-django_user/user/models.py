from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = models.CharField(_('手机号码'), max_length=11, default='', blank=True)
    memo = models.TextField(_('备注'), max_length=1024, default='', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    def __str__(self):
        if self.last_name or self.first_name:
            return self.get_full_name()
        return self.username

    class Meta:
        verbose_name = _('帐号')
        verbose_name_plural = _('帐号')
        default_permissions = ()
        permissions = (
            ('add_user', _('添加帐号')),
            ('view_user', _('查看帐号')),
            ('change_user', _('修改帐号')),
            ('delete_user', _('删除帐号')),
        )

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name}'
        return full_name.strip()
