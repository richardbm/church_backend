from django.db import models

from apps.utils.models import CustomModel


class Ministry(CustomModel):
    name = models.CharField(max_length=128)
    description = models.TextField()
    contact_information = models.OneToOneField(
        "church.Contact", blank=True, null=True, on_delete=models.SET_NULL
    )
    events = models.ManyToManyField(
        "schedule.Event", related_name="ministries", blank=True
    )

    def __str__(self):
        return self.name
