

class FieldPermissionAdminMixin:
    def get_form(self, request, obj=None, *args, **kwargs):
        form =  super().get_form(request, obj, *args, **kwargs)
        form.current_user = request.user
        return form
