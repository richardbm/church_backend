from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.accounts.models import User
from apps.accounts.tests.bakery_recipes import user_john


class UserRegistrationAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("api:v1:accounts:registration-list")
        self.user_data = {
            "email": "john@doe.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "Doe",
            "phone_number": "+56 943532346",
        }

    def test_register_user_success(self):
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="john@doe.com").exists())

    def test_register_username_already_exists(self):
        duplicated_email = "duplicatedn@doe.com"
        user_john.make(
            username=duplicated_email
        )
        data = self.user_data
        data["email"] = duplicated_email
        self.assertEqual(User.objects.filter(username=duplicated_email).count(), 1)
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.filter(username=duplicated_email).count(), 1)

    def test_register_phone_number_already_exists(self):
        duplicated_phone_number = "+56 933333333"
        user_john.make(
            phone_number=duplicated_phone_number
        )
        data = self.user_data
        data["phone_number"] = duplicated_phone_number
        self.assertEqual(User.objects.filter(phone_number=duplicated_phone_number).count(), 1)
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)
        self.assertEqual(User.objects.filter(phone_number=duplicated_phone_number).count(), 1)

    def test_register_phone_number_invalid_format(self):
        data = self.user_data
        data["phone_number"] = "933333333"
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)
        self.assertFalse(User.objects.filter(phone_number=data["phone_number"]).exists())

    def test_register_phone_number_invalid_long(self):
        data = self.user_data
        data["phone_number"] = "+5693333333"
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response)
        self.assertFalse(User.objects.filter(phone_number=data["phone_number"]).exists())
