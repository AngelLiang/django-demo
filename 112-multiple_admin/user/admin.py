from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(_UserAdmin):
    pass


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
