from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()


class CurrentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('username', 'date_joined', 'last_login')
