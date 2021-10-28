from . import views
from django.urls import path

urlpatterns = [
    path(
        'locations/<str:city>/',
        views.LocationWeatherForecastStatsAPIView.as_view(),
        name='locations'),
]
