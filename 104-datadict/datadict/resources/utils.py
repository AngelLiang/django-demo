from import_export import widgets


class AutoCreateForeginKeyWidget(widgets.ForeignKeyWidget):

    def create_instance(self, val):
        # instance = self.model.objects.create(**{self.field: val})
        instance = self.model(**{self.field: val})
        instance.save()
        # request = get_current_request()
        # log_addition(request, instance, '以导入方式添加。')
        return instance

    # def has_add_permission(self, request):
    #     return request.user.has_perm(f'{self.model._meta.app_label}.add_{self.model._meta.model_name}')

    def clean(self, value, row=None, *args, **kwargs):
        """override"""
        val = super(widgets.ForeignKeyWidget, self).clean(value)
        if val:
            # 注意去除前后空格
            if isinstance(val, str):
                val = val.strip()
            try:
                return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
            except self.model.DoesNotExist:
                return self.create_instance(val)
                # request = get_current_request()
                # if self.has_add_permission(request):
                #     return self.create_instance(val)
                # else:
                #     raise ValueError(f'没有创建{self.model._meta.verbose_name}的权限')
        else:
            return None
