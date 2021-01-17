from rest_framework import serializers

from apps.api.v1.base.serializers import BaseContactSerializer


class AboutSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    description = serializers.CharField()


class ContactSerializer(BaseContactSerializer):
    pass


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    subject = serializers.CharField()
    content = serializers.CharField()
