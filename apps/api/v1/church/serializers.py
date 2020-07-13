from rest_framework import serializers


class AboutSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    description = serializers.CharField()


class ContactParameterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(source="get_label_display")
    value = serializers.CharField()


class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    contact_parameters = ContactParameterSerializer(many=True)
