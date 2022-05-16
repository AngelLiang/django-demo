

def monkey_patch():
    from django.contrib import admin

    from river.admin import workflow
    from river.models import Workflow
    from river_patch.admin.workflow import WorkflowAdmin

    from river.core.classworkflowobject import ClassWorkflowObject
    from river_patch.core.classworkflowobject import ClassWorkflowObject as CustomClassWorkflowObject

    ClassWorkflowObject._river_driver = CustomClassWorkflowObject._river_driver
    # workflow.WorkflowAdmin = WorkflowAdmin

    admin.site.unregister(Workflow)
    admin.site.register(Workflow, WorkflowAdmin)
