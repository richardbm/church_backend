from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.blog.tests.bakery_recipes import post_published


class PostAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:blog:posts-list")

    def test_get_post_list(self):
        post = post_published.make()
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], post.title, response.data)
        self.assertEqual(
            response.data[0]["description"], post.short_description, response.data
        )

    def test_get_post_detail(self):
        post = post_published.make()
        url = reverse("api:v1:blog:posts-detail", kwargs={"slug": post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data["title"], post.title)
        self.assertEqual(response.data["description"], post.short_description)
        self.assertEqual(
            response.data["content"], post.content, response.data
        )
