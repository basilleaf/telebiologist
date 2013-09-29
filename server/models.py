from django.db import models
from django.forms import ModelForm

class Reading(models.Model):
    timestamp = models.IntegerField()
    device_id = models.IntegerField()
    trip_id = models.IntegerField()
    sensor_id = models.CharField(max_length=60)
    sensor_value = models.FloatField(max_length=60)