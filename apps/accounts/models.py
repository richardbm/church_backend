from django.db import models
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': ugettext_lazy("A user with that username already exists."),
        },
    )
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True, null=True)

