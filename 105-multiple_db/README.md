# multiple_db

django中使用多数据库示例

用户数据放在 auth_db.sqlite3 数据库，产品数据放在 primary.sqlite3 数据库，订单数据放在 order_db.sqlite3 数据库

## 准备工作

    # 初始化数据库
    python manage.py migrate --database=auth_db
    python manage.py migrate --database=order_db
    python manage.py migrate --database=primary

    # 创建管理员
    python manage.py createsuperuser --database auth_db

## 启动服务

    python manage.py runserver
