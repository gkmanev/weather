from django.db import models



class Weather(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    clouds = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()