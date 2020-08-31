from apps.blog.services import get_post, get_posts_list
from .serializers import PostListSerializer, PostDetailSerializer
from ..views import ServiceViewSet


class PostViewSet(ServiceViewSet):
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    detail_service = staticmethod(get_post)
    list_service = staticmethod(get_posts_list)
    serializer_class = PostListSerializer
    detail_serializer_class = PostDetailSerializer
