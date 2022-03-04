from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from field_permissions.admin import FieldPermissionAdminMixin
from .forms import UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAdmin(FieldPermissionAdminMixin, _UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
