from django.urls import path
from .views import WeatherListAPIView

urlpatterns = [
    path('weather/', WeatherListAPIView.as_view(), name='weather-list'),
]