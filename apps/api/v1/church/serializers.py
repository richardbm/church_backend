from rest_framework import serializers


class AboutSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=32)
