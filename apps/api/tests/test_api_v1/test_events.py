import arrow
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.events.tests.bakery_recipes import biblical_school_event
from apps.ministries.tests.bakery_recipes import ministry_biblical_school


class OccurrenceAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url_list = reverse("api:v1:events:occurrences-list")
        biblical_school_event.make()

    def test_get_occurrences_list_without_date_range(self):
        response = self.client.get(
            self.url_list, data={"start_date": "2020-07-07"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.get(
            self.url_list, data={"end_date": "2020-09-07"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_occurrences_list(self):
        response = self.client.get(
            self.url_list, data={"start_date": "2020-07-07", "end_date": "2020-09-07"}
        )
        self.check_occurrence_response(response)

    def test_get_occurrences_list_filtered_by_ministry(self):
        ministry = ministry_biblical_school.make()
        ministry.events.add(
            biblical_school_event.make()
        )
        response = self.client.get(
            self.url_list, data={"start_date": "2020-07-07", "end_date": "2020-09-07"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        response = self.client.get(
            self.url_list, data={"start_date": "2020-07-07", "end_date": "2020-09-07", "ministry_id": ministry.id}
        )
        self.check_occurrence_response(response)

    def check_occurrence_response(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(len(response.data), 5)
        right_start_dates = [
            "2020-08-08T10:00:00",
            "2020-08-15T10:00:00",
            "2020-08-22T10:00:00",
            "2020-08-29T10:00:00",
            "2020-09-05T10:00:00",
        ]
        for right_date, occurrence in zip(right_start_dates, response.data):
            self.assertEqual(arrow.get(right_date), arrow.get(occurrence["start"]))
