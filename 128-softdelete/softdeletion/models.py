# encoding=utf-8
'''
@File    :   models.py
@Time    :   2022/06/13 17:43:17
@Author  :   AngelLiang 
@Desc    :   None
'''

from collections import Counter
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import router
from django.db.models.query import QuerySet
from django.contrib.admin.utils import NestedObjects
from django.utils import timezone

from .signals import pre_softdelete, post_softdelete


class SoftDeleteCallback(object):
    def __init__(self, deleted_counter=None, using=None):
        self.deleted_counter = deleted_counter or Counter()
        self.using = using

    def delete_callback(self, obj):
        # 如果不是 SoftDeletionModelMixin 类则硬删除
        if not isinstance(obj, SoftDeletionModelMixin):
            obj.delete()
            return obj

        # 如果对象已经软删除，则进行硬删除
        # if obj.is_deleted:
        #     obj.delete()
        #     return obj

        model = obj.__class__
        if not model._meta.auto_created:
            # 发送预软删除前置信号
            pre_softdelete.send(sender=model, instance=obj, using=self.using)

        obj.soft_delete()
        # signals_to_disable： 禁止触发 pre_save 和 post_save 信号
        # obj.save(update_fields=['deleted_at'], signals_to_disable=['pre_save', 'post_save'])
        obj.save(update_fields=('deleted_at',))
        self.deleted_counter[model._meta.label] += 1

        if not model._meta.auto_created:
            # 发送软删除后置信号
            post_softdelete.send(sender=model, instance=obj, using=self.using)
        return obj


class SoftDeletableQuerySet(QuerySet):
    def delete(self):
        """Delete the records in the current QuerySet."""
        assert self.query.can_filter(), \
            "Cannot use 'limit' or 'offset' with delete."

        if self._fields is not None:
            raise TypeError(
                "Cannot call delete() after .values() or .values_list()")

        self._for_write = True
        del_query = self._chain()
        using = del_query.db

        dc = SoftDeleteCallback(using=using)
        collector = NestedObjects(using=using)
        collector.collect(del_query)
        collector.nested(dc.delete_callback)
        return sum(dc.deleted_counter.values()), dict(dc.deleted_counter)


class AllSoftDeletedManager(models.Manager):
    _queryset_class = SoftDeletableQuerySet


class UnSoftDeletedManager(AllSoftDeletedManager):
    def get_queryset(self):
        """
        Return queryset limited to not deleted entries.
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        qs = self._queryset_class(**kwargs)
        if hasattr(self.model, 'deleted_at'):
            return qs.filter(deleted_at__isnull=True)
        return qs


class SoftDeletionModelMixin(models.Model):
    """
    注意：
    1）所有关联的对象都要有软删除的操作
    2）使用 unique 的字段要加上 deleted_at 字段
    """

    class Meta:
        abstract = True

    deleted_at = models.DateTimeField(
        _('删除时间'),
        null=True,
        blank=True,
        default=None,
        db_index=True,
        editable=False
    )

    @property
    def is_deleted(self):
        return self.deleted_at is not None
    # is_deleted.short_description = '已删除'

    objects = UnSoftDeletedManager()

    def delete(self, using=None, soft=None, keep_parents=False, *args, **kwargs):
        """
        Soft delete object(set its ``is_deleted`` field to True).
        Actually delete object if setting ``soft`` to False.
        """
        using = using or router.db_for_write(self.__class__, instance=self)
        assert self.pk is not None, (
            "%s object can't be deleted because its %s attribute is set to None." %
            (self._meta.object_name, self._meta.pk.attname)
        )
        # soft 为空且 self.deleted_at 为 NULL 时， 软删除
        if soft is None:
            soft = not self.deleted_at
        if soft:
            dc = SoftDeleteCallback(using=using)
            collector = NestedObjects(using=using)
            collector.collect([self], keep_parents=keep_parents)
            collector.nested(dc.delete_callback)
            return sum(dc.deleted_counter.values()), dict(dc.deleted_counter)
        else:
            return super().delete(using=using, *args, **kwargs)

    def soft_delete(self):
        self.deleted_at = timezone.now()
