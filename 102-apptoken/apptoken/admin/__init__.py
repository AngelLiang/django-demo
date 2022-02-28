from django.contrib import admin

from .apptoken import AppTokenAdmin
from .. import models

admin.site.register(models.AppToken, AppTokenAdmin)
