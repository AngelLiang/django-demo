from django import forms


class FieldPermissionFormMixin:
    """
    ModelForm logic for removing fields when a user is found not to have change permissions.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.current_user

        model = self.Meta.model
        model_field_names = [f.name for f in model._meta.get_fields()]  # this might be too broad
        for name in model_field_names:
            if name in self.fields and not self.has_view_or_change_field_perm(user, field=name):
                self.hide_unauthorized_field(name)
            if name in self.fields and not self.has_change_field_perm(user, field=name):
                # self.remove_unauthorized_field(name)
                self.disable_unauthorized_field(name)

    def remove_unauthorized_field(self, name):
        del self.fields[name]

    def disable_unauthorized_field(self, name):
        self.fields[name].disabled = True
        # self.fields[name].widget.attrs['readonly'] = True

    def hide_unauthorized_field(self, name):
        self.fields[name].widget = self.fields[name].hidden_widget()

    def has_view_field_perm(self, user, field):
        return self.instance.has_field_perm(user, field=field, option='view')

    def has_change_field_perm(self, user, field):
        return self.instance.has_field_perm(user, field=field, option='change')

    def has_view_or_change_field_perm(self, user, field):
        return self.has_view_field_perm(user, field) or self.has_change_field_perm(user, field)


class FieldPermissionForm(FieldPermissionFormMixin, forms.ModelForm):
    pass
