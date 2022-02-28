FROM centos:7

# 设置环境变量
ENV LANG=en_US.UTF-8 LC_ALL=en_US.utf8
# 设置时区
RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 配置环境，同时可以安装其他依赖包
RUN yum install -y epel-release python36 python36-pip

# Set environment variables
# 阻止 Python 生成.pyc文件、阻止段错误上启用 Python 回溯
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONFAULTHANDLER=1

WORKDIR /usr/src/app

COPY . .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install pipenv -i https://mirrors.aliyun.com/pypi/simple/
RUN pipenv install --deploy --system
# 把静态文件收集到本地
RUN DJANGO_SETTINGS_MODULE=proj.settings python3 manage.py collectstatic --noinput

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD ["waitress-serve", "--listen=0.0.0.0:8000", "proj.wsgi:application"]
