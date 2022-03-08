from django import forms

from django.contrib.auth.forms import UserCreationForm as _UserCreationForm
from django.contrib.auth.forms import UserChangeForm as _UserChangeForm
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

from field_permissions.forms import FieldPermissionFormMixin


class UserCreationForm(_UserCreationForm):
    # is_staff = forms.BooleanField(label=_('人员状态'), initial=True)

    class Meta(_UserCreationForm.Meta):
        fields = ("username", 'is_staff')


class UserChangeForm(FieldPermissionFormMixin, _UserChangeForm):

    class Meta(_UserChangeForm.Meta):
        pass

