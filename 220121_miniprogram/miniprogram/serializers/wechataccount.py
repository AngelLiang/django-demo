from rest_framework import serializers

from ..models import WeChatAccount


class WeChatAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeChatAccount
        fields = '__all__'
        extra_kwargs = {
            'openId': {'write_only': True},
            'session_key': {'write_only': True},
            'unionId': {'write_only': True}
        }
