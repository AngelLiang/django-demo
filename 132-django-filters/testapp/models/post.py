from decimal import Decimal

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField('标签名', max_length=32, index=True)

    def __str__(self):
        return self.name

    class Meta:
        """
        https://docs.djangoproject.com/en/2.2/topics/db/models/#meta-options
        https://docs.djangoproject.com/en/2.2/ref/models/options/#model-meta-options
        """
        # https://docs.djangoproject.com/en/2.2/ref/models/options/#django.db.models.Options.verbose_name
        verbose_name = '标签'
        verbose_name_plural = verbose_name

        # https://docs.djangoproject.com/en/2.2/ref/models/options/#default-permissions
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_tag', _('允许添加标签')),
            ('view_tag', _('允许查看标签')),
            ('change_tag', _('允许修改标签')),
            ('delete_tag', _('允许删除标签')),

            # for django-import-export
            ('import_tag', _('允许导入标签')),
            ('export_tag', _('允许导出标签')),
        )


        # https://docs.djangoproject.com/en/2.2/ref/models/options/#unique-together
        # unique_together =
        # db_table = 'tag'


class Post(BaseModel):
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#charfield
    title = models.CharField('标题', max_length=128)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#slugfield
    slug = models.SlugField(default='')

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#textfield
    content = models.TextField('内容', default='')

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#booleanfield
    is_delete = models.BooleanField('已删除', default=False, db_index=True)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#datefield
    create_date = models.DateField('创建日期', auto_now_add=True)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#timefield
    create_time = models.TimeField('创建时间', auto_now_add=True)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#datetimefield
    update_datetime = models.DateTimeField('更新时间', auto_now=True)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#integerfield
    view_count = models.IntegerField('浏览次数', default=0)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#decimalfield
    money = models.DecimalField(max_digits=8, decimal_places=2, blank=True, default=Decimal('0.0'))

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#floatfield
    price = models.FloatField(blank=True, default=0.0)

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey.on_delete: CASCADE/PROTECT/SET_NULL/SET_DEFAULT/SET()/DO_NOTHING
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='用户',
        # related_name='+',
    )

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#manytomanyfield
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices
    DRAFT = 'D'
    PUBLISH = 'P'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISH, 'Publish'),
    ]

    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=DRAFT
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_datetime']
        verbose_name = '文章'
        verbose_name_plural = verbose_name
