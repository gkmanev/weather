from rest_framework import generics
from .models import Weather
from .serializers import WeatherSerializer

class WeatherListAPIView(generics.ListAPIView):
    serializer_class = WeatherSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)        
        if lat is not None and long is not None:
            queryset = Weather.objects.filter(lat=lat, long=long)
        else:
            queryset = Weather.objects.all()
        return queryset
