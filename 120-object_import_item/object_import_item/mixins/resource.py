
import tablib
from django.utils.encoding import force_str


class ItemResourceMixin:
    master_id_field = 'master_id'

    def __init__(self, request=None):
        self.request = request
        super().__init__()

    def get_master_id(self):
        return self.request.GET.get('master_id') if self.request else None

    def init_instance(self, row=None):
        instance = super().init_instance(row)
        master_id = self.get_master_id()
        setattr(instance, self.master_id_field, master_id)
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

    def get_template(self, *args, **kwargs):
        """获取导入模板"""
        headers = self.get_template_headers()
        data = tablib.Dataset(headers=headers)
        return data

    def get_template_fields(self):
        """模板字段，可以返回一个列表，格式为 [self.fields[f],]
        """
        return self.get_import_fields()

    def get_template_headers(self):
        """导入模板头部"""
        headers = [force_str(field.column_name)
                   for field in self.get_template_fields()]
        return headers
