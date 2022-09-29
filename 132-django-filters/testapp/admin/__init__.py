from django.contrib import admin

from .. import models
from .testapp import TestappAdmin


admin.site.register(models.Testapp, TestappAdmin)
