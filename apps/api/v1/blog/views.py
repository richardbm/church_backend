from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.blog.services import get_post, get_posts_list
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(ViewSet):
    lookup_field = 'slug'
    permission_classes = (AllowAny,)

    def retrieve(self, request, slug=None):
        post = get_post(slug=slug)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostDetailSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        queryset = get_posts_list()
        serializer = PostListSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
