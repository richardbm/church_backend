from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy
from phonenumber_field.modelfields import PhoneNumberField

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
        (CONTACT_PARAMETER_PHONE_NUMBER, "Phone number"),
        (CONTACT_PARAMETER_EMAIL, "Email"),
        (CONTACT_PARAMETER_MAP, "Map"),
    )
    label = models.CharField(choices=LABEL_CHOICE, max_length=32)
    value = models.CharField(max_length=128)
    contact = models.ForeignKey(
        "Contact", related_name="contact_parameters", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("label",)

    def __str__(self):
        return self.label


class News(CustomModel):
    subject = models.CharField(max_length=140)
    content = models.TextField()
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Membership(CustomModel):
    first_name = models.CharField(ugettext_lazy("first name"), max_length=30)
    last_name = models.CharField(ugettext_lazy("last name"), max_length=150)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True, null=True)
    member_since = models.DateTimeField(default=datetime.now)
    user = models.OneToOneField(
        "accounts.User",
        blank=True,
        null=True,
        related_name="user",
        on_delete=models.SET_NULL,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.id} - {self.full_name}"


class MemberMinistry(CustomModel):
    MEMBER_TYPE_CHOICE = (
        ("DISCIPLE", ugettext_lazy("CHURCH_MEMBER_TYPE_DISCIPLE")),
        ("COLLABORATOR", ugettext_lazy("CHURCH_MEMBER_TYPE_COLLABORATOR")),
        ("LEADER", ugettext_lazy("CHURCH_MEMBER_TYPE_LEADER")),
    )
    member = models.ForeignKey(
        Membership, related_name="ministries", on_delete=models.CASCADE
    )
    ministry = models.ForeignKey(
        "ministries.Ministry", related_name="members", on_delete=models.PROTECT
    )
    member_type = models.CharField(max_length=16, choices=MEMBER_TYPE_CHOICE)
    is_baptized = models.BooleanField()
