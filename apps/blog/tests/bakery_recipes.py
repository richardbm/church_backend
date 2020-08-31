from model_bakery.recipe import Recipe, foreign_key

from apps.blog.constants import POST_STATUS_PUBLISHED
from apps.blog.models import Post


post_published = Recipe(
    Post,
    title="How to prepare a speech",
    slug="how-to-prepare-a-speech-123456",
    short_description="How to prepare a speech...",
    content="How to prepare a speech...",
    status=POST_STATUS_PUBLISHED,
    published_at="2020-08-08T00:00:00Z"
)
