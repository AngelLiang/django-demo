from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from ..models import Testapp


class TestappSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testapp
        fields = '__all__'
