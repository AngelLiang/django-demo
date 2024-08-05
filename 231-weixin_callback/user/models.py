from django.db import models
from utils.strings import generate_random_string


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=11, db_index=True)
    openid = models.CharField(max_length=255, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    key = models.CharField(primary_key=True, max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_token'

    def generate_key(self):
        self.key = generate_random_string(64)
