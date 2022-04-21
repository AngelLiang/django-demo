from django.db import models
from django.db.models import PROTECT
from django.utils.translation import ugettext_lazy as _

from river.config import app_config
from river.models import BaseModel, State
from river.models.managers.workflowmetada import WorkflowManager


class Workflow(BaseModel):
    class Meta:
        app_label = 'river'
        verbose_name = _("工作流程")
        verbose_name_plural = _("工作流程")
        unique_together = [("content_type", "field_name")]

    objects = WorkflowManager()

    content_type = models.ForeignKey(app_config.CONTENT_TYPE_CLASS, verbose_name=_('Content Type'), on_delete=PROTECT)
    field_name = models.CharField(_("Field Name"), max_length=200)
    initial_state = models.ForeignKey(State, verbose_name=_("Initial State"),
                                      related_name='workflow_this_set_as_initial_state', on_delete=PROTECT)

    def natural_key(self):
        return self.content_type.natural_key() + (self.field_name,)
    natural_key.dependencies = ['contenttypes.ContentType']

    def __str__(self):
        if self.content_type:
            return "%s.%s" % (self.content_type.model, self.field_name)
        return super().__str__()
