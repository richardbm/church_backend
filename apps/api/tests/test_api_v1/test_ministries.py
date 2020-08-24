from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.ministries.tests.bakery_recipes import ministry_biblical_school


class MinistryAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:ministries:ministries-list")

    def test_get_ministries_list(self):
        ministry = ministry_biblical_school.make()
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], ministry.name, response.data)
        self.assertEqual(
            response.data[0]["description"], ministry.description, response.data
        )
        self.assertEqual(
            response.data[0]["contact_information"]["name"],
            ministry.contact_information.name,
            response.data,
        )

    def test_get_ministry_detail(self):
        ministry = ministry_biblical_school.make()
        url = reverse("api:v1:ministries:ministries-detail", kwargs={"pk": ministry.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["name"], ministry.name)
        self.assertEqual(response.data["description"], ministry.description)
        self.assertEqual(
            response.data["contact_information"]["name"],
            ministry.contact_information.name,
            response.data,
        )
