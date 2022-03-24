from river.models.managers.rivermanager import RiverManager
from river.config import app_config


class WorkflowManager(RiverManager):
    def get_by_natural_key(self, app_label, model, field_name):
        return self.get(content_type__app_label=app_label, content_type__model=model, field_name=field_name)
