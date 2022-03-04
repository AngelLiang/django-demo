from django.contrib import admin

from .workflow import WorkflowAdmin
from .state import StateAdmin
from .transitionmeta import TransitionMetaAdmin
from .transitionapprovalmeta import TransitionApprovalMetaAdmin
from .transition import TransitionAdmin

from .transitionapproval import TransitionApprovalAdmin
from .function_admin import FunctionAdmin
from .hook_admins import OnApprovedHookAdmin, OnTransitHookAdmin, OnCompleteHookAdmin

from .. import models

admin.site.register(models.Workflow, WorkflowAdmin)
admin.site.register(models.State, StateAdmin)
admin.site.register(models.TransitionMeta, TransitionMetaAdmin)
admin.site.register(models.TransitionApprovalMeta, TransitionApprovalMetaAdmin)
admin.site.register(models.Transition, TransitionAdmin)
admin.site.register(models.TransitionApproval, TransitionApprovalAdmin)
admin.site.register(models.Function, FunctionAdmin)

admin.site.register(models.OnApprovedHook, OnApprovedHookAdmin)
admin.site.register(models.OnTransitHook, OnTransitHookAdmin)
admin.site.register(models.OnCompleteHook, OnCompleteHookAdmin)
