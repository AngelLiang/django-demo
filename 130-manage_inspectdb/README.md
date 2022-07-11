# manage inspectdb

## 准备工作

    python manage.py migrate

## 使用 inspectdb 命令创建 model

    # 获取指定数据表的模型
    python manage.py inspectdb <model_name>

    # 生成所有模型到 testapp/models.py
    python manage.py inspectdb > testapp/models.py

之后可以在 testapp/models.py 看到 user 模型
