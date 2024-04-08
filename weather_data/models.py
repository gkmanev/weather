from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from pytz import timezone

class TodayManager(models.Manager):
    def get_queryset(self):
        today = datetime.now(timezone('Europe/London')).date()
        tomorrow = today + timedelta(1)
        today_start = str(today)+'T'+'00:00:00Z'
        today_end = str(tomorrow)+'T'+'00:00:00Z'
        return super().get_queryset().filter(timestamp__gt = today_start, timestamp__lt = today_end)
    


class Weather(models.Model):
    timestamp = models.DateTimeField(default = datetime.now())
    temperature = models.FloatField()
    clouds = models.IntegerField()
    heatindex = models.FloatField(default=0)
    uv = models.IntegerField(default=0)
    lat = models.FloatField()
    long = models.FloatField()
    today = TodayManager()
    objects = models.Manager()