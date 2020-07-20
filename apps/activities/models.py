from django.db import models

from apps.utils.models import CustomModel


class Activity(CustomModel):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
