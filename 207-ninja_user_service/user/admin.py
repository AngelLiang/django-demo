from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from user.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        # 个人信息
        (_('Personal info'), {'fields': ('first_name',
                                         'last_name', 'email', 'phone')}),
        # 权限
        (_('Permissions'), {'fields': (
            'groups',
            'user_permissions',
        )}),
        (_('状态'), {'fields': (
            'is_active', 'is_staff', 'is_superuser',
        )}),
        # 重要日期
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = [
        'last_login', 'date_joined',
    ]

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2', 'is_staff'),
    #     }),
    # )


admin.site.register(User, UserAdmin)
