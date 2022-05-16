
使用模板生成django项目目录

    django-admin startproject --template=startproject_template proj .
    pipenv install -r config\requirements.txt

    # 部署启动
    python manage.py collectstatic
    waitress-serve --listen=0.0.0.0:8000 config.wsgi:application
