from django import forms

from ..models import Testapp


class TestappForm(forms.ModelForm):

    class Meta:
        model = Testapp
        fields = '__all__'
