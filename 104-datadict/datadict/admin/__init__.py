from django.contrib import admin

from .datadict import DataDictAdmin
from .datadictitem import DataDictItemAdmin


from .. import models

admin.site.register(models.DataDict, DataDictAdmin)
# admin.site.register(models.DataDictItem, DataDictItemAdmin)
