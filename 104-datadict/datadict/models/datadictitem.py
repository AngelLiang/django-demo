from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataDictItem(models.Model):
    master = models.ForeignKey(
        'DataDict',
        verbose_name=_("数据字典"),
        on_delete=models.CASCADE,
        db_constraint=False,
        related_name='items',
    )
    code = models.CharField(_("编码"), max_length=40)
    label = models.CharField(_("标签"), max_length=128, blank=True, default="")

    class Meta:
        verbose_name = _('字典明细')
        verbose_name_plural = _('字典明细')
        # unique_together = ('master', 'code')
        default_permissions = ()
        permissions = (
            # 功能权限
            ('add_dictdataitem', _('允许添加字典明细')),
            ('view_dictdataitem', _('允许查看字典明细')),
            ('change_dictdataitem', _('允许修改字典明细')),
            ('delete_dictdataitem', _('允许删除字典明细')),
            ('import_dictdataitem', _('允许导入字典明细')),
            ('export_dictdataitem', _('允许导出字典明细')),
        )

    def __str__(self):
        return self.code
