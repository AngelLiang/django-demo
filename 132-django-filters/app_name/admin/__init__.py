from django.contrib import admin

from .. import models
from .{{app_name}} import {{camel_case_app_name}}Admin


admin.site.register(models.{{camel_case_app_name}}, {{camel_case_app_name}}Admin)
