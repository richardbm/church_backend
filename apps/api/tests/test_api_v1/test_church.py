from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from apps.church.constants import (
    CONTACT_PARAMETER_PHONE_NUMBER,
    CONTACT_PARAMETER_EMAIL,
)
from apps.church.tests.bakery_recipes import (
    about_mission,
    about_vision,
    about_history,
    contact_workship,
    contact_jane_doe,
    contact_john_doe,
)


class AboutAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:church:about-list")

    def test_get_about_list(self):
        history = about_history.make(order=3)
        vision = about_vision.make(order=2)
        mission = about_mission.make(order=1)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["label"], mission.label, response.data)
        self.assertEqual(response.data[1]["label"], vision.label, response.data)
        self.assertEqual(response.data[2]["label"], history.label, response.data)

    def test_get_about_detail(self):
        about_vision.make()
        mission = about_mission.make()
        url = reverse("api:v1:church:about-detail", kwargs={"pk": mission.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["label"], mission.label)
        self.assertEqual(response.data["description"], mission.description)


class ContactAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:church:contact-list")

    def test_get_contact_list(self):
        workship = contact_workship.make(order=3)
        jane_doe = contact_jane_doe.make(order=2)
        john_doe = contact_john_doe.make(order=1)
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["name"], john_doe.name, response.data)
        self.assertEqual(response.data[1]["name"], jane_doe.name, response.data)
        self.assertEqual(response.data[2]["name"], workship.name, response.data)

    def test_get_about_detail(self):
        john_doe = contact_john_doe.make(order=1)
        contact_jane_doe.make(order=2)
        baker.make(
            "church.ContactParameter",
            label=CONTACT_PARAMETER_PHONE_NUMBER,
            value="+56 912345678",
            contact=john_doe,
        )

        baker.make(
            "church.ContactParameter",
            label=CONTACT_PARAMETER_EMAIL,
            value="john@doe.com",
            contact=john_doe,
        )

        url = reverse("api:v1:church:contact-detail", kwargs={"pk": john_doe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["name"], john_doe.name)
        self.assertEqual(response.data["description"], john_doe.description)
        self.assertEqual(len(response.data["contact_parameters"]), 2)
