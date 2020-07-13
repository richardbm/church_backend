from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.accounts.models import User
from apps.accounts.tests.bakery_recipes import user_john
from apps.church.tests.bakery_recipes import about_mission, about_vision, about_history


class AboutAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:church:about-list")
        self.user_data = {
            "email": "john@doe.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "Doe",
            "phone_number": "+56 943532346",
        }

    def test_get_about_list(self):
        history = about_history.make(order=3)
        vision = about_vision.make(order=2)
        mission = about_mission.make(order=1)
        response = self.client.get(self.url_list, data=self.user_data)
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
