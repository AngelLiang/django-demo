from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        label=_('旧密码'),
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    new_password = serializers.CharField(
        label=_('新密码'),
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    new_password_confirm = serializers.CharField(
        label=_('确认新密码'),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('旧密码错误')
        return value

    # def validate_new_password_confirm(self, value):
    #     if self.data['new_password'] != self.data['new_password_confirm']:
    #         raise serializers.ValidationError('两次密码不一致')
    #     return value

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError('两次密码不一致')
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
