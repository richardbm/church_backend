from rest_framework import serializers

from apps.api.v1.base.serializers import BaseContactSerializer


class ContactSerializer(BaseContactSerializer):
    pass


class MinistrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    contact_information = ContactSerializer(read_only=True, allow_null=True)

