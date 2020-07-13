from django.db.models import QuerySet

from apps.church.models import About


def get_about_list() -> QuerySet:
    return About.objects.filter(is_active=True).order_by("order")


def get_about(about_id: int = None) -> About:
    return About.objects.filter(pk=about_id, is_active=True).first()
