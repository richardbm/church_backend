from typing import Dict

from apps.accounts.models import User


def create_user(data: Dict) -> User:
    return User.objects.create_user(
        **data
    )


def get_user(**kwargs: Dict) -> User:
    return User.objects.filter(**kwargs).first()
