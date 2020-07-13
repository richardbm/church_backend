from django.db import models

from apps.church.constants import (
    CONTACT_PARAMETER_ADDRESS,
    CONTACT_PARAMETER_PHONE_NUMBER,
    CONTACT_PARAMETER_EMAIL,
    CONTACT_PARAMETER_MAP,
)
from apps.utils.models import CustomModel


class About(CustomModel):
    label = models.CharField(max_length=128)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Contact(CustomModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ContactParameter(CustomModel):
    LABEL_CHOICE = (
        (CONTACT_PARAMETER_ADDRESS, "Address"),
        (CONTACT_PARAMETER_PHONE_NUMBER, "Phone_number"),
        (CONTACT_PARAMETER_EMAIL, "Email"),
        (CONTACT_PARAMETER_MAP, "Map"),
    )
    label = models.CharField(choices=LABEL_CHOICE, max_length=32)
    contact = models.ForeignKey(
        "Contact", related_name="contact_parameters", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.label
