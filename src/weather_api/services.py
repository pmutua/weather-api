# importing "collections" for deque operations
import collections
import statistics

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
import requests


BASE_URL = settings.WEATHER_API_BASE_URL
API = BASE_URL + \
    "/forecast.json?key={api_key}&q={city}&days={days}&aqi=no&alerts=no"


class WeatherAPIService:
    """Service class for interfacing with Weather API Service."""

    def get_weather_forcast(city, days):
        """Queries the weather API and returns the weather data for a
            particular city.
        """
        try:
            url = API.format(
                city=city,
                api_key=settings.WEATHER_API_KEY,
                days=days)
            response = requests.get(url)

            data = response.json()['forecast']['forecastday']

            temperatures_deque = collections.deque([])

            for item in data:
                for hour in item['hour']:
                    temperatures_deque.append(hour['temp_c'])

            temp_list = list(temperatures_deque)

            average_temp = statistics.mean(temp_list)
            median_temp = statistics.median(temp_list)
            max_temp = max(temp_list)
            min_temp = min(temp_list)
            json = {
                "maximum": max_temp,
                "minimum": min_temp,
                "average": average_temp,
                "median": median_temp
            }

            return {
                'success': True,
                "msg": "success",
                "data": json,
                "status": status.HTTP_200_OK}
        except Exception as e:
            return {
                'success': False,
                "data": None,
                "msg": f'Error {str(e)}',
                "status": status.HTTP_400_BAD_REQUEST}
