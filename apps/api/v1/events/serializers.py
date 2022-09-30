from rest_framework import serializers

from apps.api.v1.ministries.serializers import MinistrySerializer


class OccurrenceSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    start = serializers.DateTimeField(read_only=True)
    end = serializers.DateTimeField(read_only=True)
    existed = serializers.BooleanField(read_only=True)
    event_id = serializers.IntegerField(read_only=True)
    color = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    ministries = serializers.ListField(child=MinistrySerializer(), read_only=True)
    cancelled = serializers.BooleanField(read_only=True)

