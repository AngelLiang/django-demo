import os
import random
import string
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from django.contrib.auth.models import User

for i in range(1, 1000):
	# 从数字和字母中随机取8个字符作为用户名
    s = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    User.objects.create_user(s, s, s).save()
