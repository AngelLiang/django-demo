# django实现软删除

## 功能

- model 实现软删除
- 支持级联软删除
- admin 后台的删除改为软删除
- 软删除的数据不在 admin 中显示


## 快速开始

    poetry install
    poetry shell

    # 创建管理员
    python manage.py createsuperuser

    # 启动服务
    python manage.py runserver

## 使用方法

1、 配置 settings.py
```
# settings.py
INSTALLED_APPS = [
    ...
    'softdeletion',
]
```

2、 添加 SoftDeletionModelMixin 
```
from django.db import models
from softdeletion.models import SoftDeletionModelMixin


class CustomModel(SoftDeletionModelMixin, models.Model):
    ...

```

3、 如果需要定制 Manager ，需要继承 UnSoftDeletedManager

```
from softdeletion.models import UnSoftDeletedManager


class CustomManager(UnSoftDeletedManager):
    pass


class CustomModel(SoftDeletionModelMixin, models.Model):
    ...

    objects = CustomManager()

```

## 参考资料

- https://github.com/alextanhongpin/database-design/blob/master/soft-delete.md
