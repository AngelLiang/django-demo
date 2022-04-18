

class ItemResourceMixin:
    master_id_field = 'master_id'

    def __init__(self, request):
        self.request = request
        super().__init__()

    def get_master_id(self):
        return self.request.GET.get('master_id')

    def init_instance(self, row=None):
        instance = super().init_instance(row)
        master_id=self.get_master_id()
        setattr(instance, self.master_id_field,master_id)
        return instance

    def get_instance(self, instance_loader, row):
        import_id_fields = [
            self.fields[f] for f in self.get_import_id_fields()
        ]
        for field in import_id_fields:
            if field.column_name not in row:
                return

        try:
            params = {self.get_master_id_field: self.get_master_id()}
            for key in self.get_import_id_fields():
                field = self.fields[key]
                params[field.attribute] = field.clean(row)
            if params:
                return self.get_queryset().get(**params)
            else:
                return None
        except self._meta.model.DoesNotExist:
            return None
