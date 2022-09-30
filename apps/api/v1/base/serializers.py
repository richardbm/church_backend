from rest_framework import serializers


class ContactParameterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField(read_only=True, source="get_label_display")
    value = serializers.CharField(read_only=True)


class BaseContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    contact_parameters = ContactParameterSerializer(read_only=True, many=True)
