from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_('用户名'))
    password = serializers.CharField(
        label=_('密码'),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class TokenResponseDataSerializer(serializers.Serializer):
    token = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField(label='业务码')
    self = serializers.CharField(label='当前URL')
    data = TokenResponseDataSerializer()


class TokenDestroyResponseSerializer(serializers.Serializer):
    code = serializers.IntegerField(label='业务码')
    self = serializers.CharField(label='当前URL')
