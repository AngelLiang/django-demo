from rest_framework import serializers


class ResponseCodeSerializer(serializers.Serializer):
    code = serializers.CharField(label='业务玛')
    _self = serializers.CharField(label='URL地址')
