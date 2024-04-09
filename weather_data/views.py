from rest_framework import generics
from .models import Weather
from .serializers import WeatherSerializer

class WeatherListAPIView(generics.ListAPIView):
    serializer_class = WeatherSerializer

    def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)    
        date_range = self.request.query_params.get('date_range', None)           
        if lat is not None and long is not None:
            if date_range == 'today':
                queryset = Weather.today.filter(lat__startswith=str(lat)[:2], long__startswith=str(long)[:2]).order_by("timestamp")
            elif date_range == 'month':
                queryset = Weather.month.filter(lat__startswith=str(lat)[:2], long__startswith=str(long)[:2]).order_by("timestamp")
            else:
                queryset = Weather.year.filter(lat__startswith=str(lat)[:2], long__startswith=str(long)[:2]).order_by("timestamp")
        return queryset
