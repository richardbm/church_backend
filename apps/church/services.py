from django.db.models import QuerySet

from apps.church.models import About, Contact, News


def get_about_list() -> QuerySet:
    return About.objects.filter(is_active=True).order_by("order")


def get_about(about_id: int = None) -> About:
    return About.objects.filter(pk=about_id, is_active=True).first()


def get_contact_list() -> QuerySet:
    return Contact.objects.filter(is_active=True).order_by("order")


def get_contact(contact_id: int = None) -> Contact:
    return Contact.objects.filter(pk=contact_id, is_active=True).first()


def get_news_list() -> QuerySet:
    return News.objects.filter(is_active=True).order_by("order")


def get_news_detail(news_id: int = None) -> News:
    return News.objects.filter(pk=news_id, is_active=True).first()
