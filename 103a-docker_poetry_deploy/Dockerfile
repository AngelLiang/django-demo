FROM centos:7

# 设置环境变量
ENV LANG=en_US.UTF-8 LC_ALL=en_US.utf8
# 设置时区
RUN ln -s -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN yum install -y epel-release \
    python36 python36-pip python3-devel \
    mysql-devel gcc pango git

# Set environment variables
# 阻止 Python 生成.pyc文件、阻止段错误上启用 Python 回溯
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONFAULTHANDLER=1

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy local code to the container image.
COPY . .

RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry -i https://mirrors.aliyun.com/pypi/simple/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry run python3 manage.py collectstatic --noinput

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD ["poetry", "run", "waitress-serve", "--listen=0.0.0.0:8000", "proj.wsgi:application"]
