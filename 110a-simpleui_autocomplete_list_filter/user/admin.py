from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

from autocomplete_light_utils.admin import AutocompleteLightModelAdminMixin


class CustomUserAdmin(AutocompleteLightModelAdminMixin, UserAdmin):
    pass


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
