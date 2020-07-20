from typing import Iterable

from apps.ministries.models import Ministry


def get_ministries_list() -> Iterable[Ministry]:
    return Ministry.objects.filter(is_active=True)


def get_ministry(ministry_id: int = None) -> Ministry:
    return Ministry.objects.filter(pk=ministry_id, is_active=True).first()
