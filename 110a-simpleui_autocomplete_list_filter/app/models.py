from django.db import models

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    title = models.CharField(_('标题'), max_length=40)
    content = models.TextField(_('内容'), default='', blank=True)
    is_public = models.BooleanField(_('已发布'), False)

    created_at = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新时间'), auto_now=True)

    creator = models.ForeignKey(
        User,
        verbose_name=_('创建者'),
        on_delete=models.CASCADE,
        related_name='+',
        db_constraint=False,
    )

    class Meta:
        verbose_name = _('文章')
        verbose_name_plural = _('文章')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_post', _('允许添加文章')),
            ('view_post', _('允许查看文章')),
            ('change_post', _('允许修改文章')),
            ('delete_post', _('允许删除文章')),
        )

    def __str__(self):
        return self.title

    def natural_key(self):
        """That method should always return a natural key tuple"""
        return (self.title,)
