from django.contrib import admin

from . import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


admin.site.register(models.UserProfile, UserProfileAdmin)
