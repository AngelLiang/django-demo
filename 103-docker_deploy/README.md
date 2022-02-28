# docker deploy

使用docker部署django（基于postgresql数据库）

## 快速开始

    docker-compose up -d --build

    docker-compose exec dj python3 manage.py migrate
    docker-compose exec dj python3 manage.py createsuperuser

启动后访问 http://127.0.0.1:8000/ 即可

## 注意事项

1. psycopg2-binary依赖包要小于2.9，否则可能出现数据库链接错误
2. 如果数据库因为没有设置 `POSTGRES_PASSWORD` 环境变量无法启动，可以试试重新部署

## 参考

- https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
