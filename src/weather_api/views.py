from rest_framework import views
from rest_framework.response import Response
from .services import WeatherAPIService


class LocationWeatherForecastStatsAPIView(views.APIView):
    """
    This view provides `GET` method minimum, maximum,
    average and median temperature for a given city.
    """

    def get(self, request, city):
        """
        Returns the minimum, maximum, average and median temperature for a
        given city.

        GET example: http://example.com/api/locations/london/?days=1
        """
        days_query = request.GET.get('days')
        res = WeatherAPIService.get_weather_forcast(city, days_query)
        if res['success']:
            return Response(data=res, status=res['status'])
        return Response(data=res, status=res['status'])
