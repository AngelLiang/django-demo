from django.contrib import admin

from import_export.admin import ImportExportMixin
from import_export.admin import ImportExportActionModelAdmin
from import_export.formats.base_formats import JSON

from .workflowinline import TransitionApprovalMetaInline, TransitionMetaInline
from ..resources.workflow import WorkflowResource
from river.admin import WorkflowAdmin
# noinspection PyMethodMayBeStatic


class WorkflowAdmin(ImportExportMixin,
                    ImportExportActionModelAdmin,
                    WorkflowAdmin):
    inlines = (TransitionMetaInline, TransitionApprovalMetaInline)
    formats = (JSON,)
    resource_class = WorkflowResource
