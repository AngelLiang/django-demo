from river.models.managers.rivermanager import RiverManager
from ..workflow import Workflow
from ..state import State


class TransitionMetadataManager(RiverManager):
    def get_by_natural_key(self, app_label, model, field_name, source_state, destination_state):
        wf = Workflow.objects.get_by_natural_key(app_label, model, field_name)
        # print((wf, source_state, destination_state))
        if isinstance(source_state, State):
            ss = source_state
        else:
            ss = State.objects.get_by_natural_key(source_state)
        if isinstance(destination_state, State):
            ds = destination_state
        else:
            ds = State.objects.get_by_natural_key(destination_state)
        return self.get(workflow=wf, source_state=ss, destination_state=ds)


class TransitionApprovalMetadataManager(RiverManager):
    def get_by_natural_key(self, app_label, model, field_name, source_state, destination_state, priority):
        from ..transitionmeta import TransitionMeta
        wf = Workflow.objects.get_by_natural_key(app_label, model, field_name)
        tm = TransitionMeta.objects.get_by_natural_key(app_label, model, field_name, source_state, destination_state)
        return self.get(workflow=wf, transition_meta=tm, priority=priority)
