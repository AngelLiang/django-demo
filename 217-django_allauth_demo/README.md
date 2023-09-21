# django-allauth-demo

填写 oauth 配置

Homepage URL： http://127.0.0.1:8000
Authorization callback URL： http://127.0.0.1:8000


1、启动服务

```
python manage.py runserver
```

2、访问 http://127.0.0.1:8000/accounts/login/ ，使用github登录

Github 社交登录之后会重定向到 http://127.0.0.1:8000/accounts/profile/ 。
