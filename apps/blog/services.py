from typing import Iterable

from .constants import POST_STATUS_PUBLISHED
from .models import Post


def get_posts_list() -> Iterable[Post]:
    return Post.objects.filter(is_active=True, status=POST_STATUS_PUBLISHED)


def get_post(post_id: int = None, slug: str = None) -> Post:
    assert post_id or slug, "it must receiver either post_id or slug"
    posts = Post.objects.filter()
    if post_id:
        posts = posts.filter(pk=post_id)
    if slug:
        posts = posts.filter(slug=slug)
    return posts.filter(is_active=True, status=POST_STATUS_PUBLISHED).first()
