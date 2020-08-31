from rest_framework import serializers


class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(source="get_description")


class PostDetailSerializer(PostListSerializer):
    content = serializers.CharField(read_only=True)

