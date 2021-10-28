from django.urls import reverse
from django.conf import settings
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


BASE_URL = settings.WEATHER_API_BASE_URL
API = BASE_URL + \
    "/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"


class LocationWeatherForecastStatsTestCase(APITestCase):
    """ Test module for GET LocationWeatherForecastStats API """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        cls.city = "London"
        # Create an instance of a GET request
        cls.locations_url = reverse('locations', args=[cls.city]) + '?days=4'

    def test_get_min_max_avg_median_temperature(self):
        """The endpoint returns a status 200."""

        response = self.client.get(self.locations_url)

        # Check status response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
