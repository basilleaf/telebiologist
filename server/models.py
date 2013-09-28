from django.db import models
from django.forms import ModelForm

class Reading(models.Model):
    timestamp = models.IntegerField()
    device_id = models.IntegerField()
    trip_id = models.IntegerField()
    sensor_id = models.CharField()
    sensor_value = models.CharField()