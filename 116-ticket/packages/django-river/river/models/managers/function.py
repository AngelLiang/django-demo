from river.models.managers.rivermanager import RiverManager


class FunctionManager(RiverManager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
