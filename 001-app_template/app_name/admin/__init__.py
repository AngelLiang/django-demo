from django.contrib import admin

from .{{app_name}} import {{camel_case_app_name}}Admin
from . import models


admin.site.register({{camel_case_app_name}}, {{camel_case_app_name}}Admin)
