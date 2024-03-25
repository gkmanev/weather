# weather_data/serializers.py
from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'timestamp', 'temperature', 'clouds', 'lat', 'long']