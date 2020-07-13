from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.utils.models import CustomModel


class Ministry(CustomModel):
    name = models.CharField(max_length=128)
    description = models.TextField()
    contact_info = models.OneToOneField(
        "church.Contact", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
