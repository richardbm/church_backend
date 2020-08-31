from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from .constants import POST_STATUS_PUBLISHED, POST_STATUS_DRAFT
from ..utils.html import get_read_time, extract_short_description
from ..utils.html import get_markdown_from_html
from ..utils.models import CustomModel
from ..utils.slugs import create_unique_slug


class Post(CustomModel):
    STATUS_CHOICES = (
        (POST_STATUS_DRAFT, POST_STATUS_DRAFT),
        (POST_STATUS_PUBLISHED, POST_STATUS_PUBLISHED),
    )
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(null=True, blank=True)
    short_description = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="posts")
    read_time = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default=POST_STATUS_PUBLISHED)
    published_at = models.DateTimeField(blank=True, null=True)

    def get_description(self):
        if self.short_description:
            return self.short_description
        return extract_short_description(self.content)

    def __str__(self):
        return self.title


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)

    if instance.content:
        html_string = get_markdown_from_html(instance.content)
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


# This is a pre_save only because we are using django admin.
# This must be done into a service once we have a custom api for content management
pre_save.connect(pre_save_post_receiver, sender=Post)
