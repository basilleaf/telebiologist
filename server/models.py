from django.db import models
from django.forms import ModelForm


class Reading(models.Model):

    timestamp = models.IntegerField(null=True, blank=True)
    device_id = models.IntegerField(null=True, blank=True)
    trip_id = models.IntegerField(null=True, blank=True)
    sensor_id = models.CharField(max_length=60)
    sensor_value = models.FloatField(max_length=60)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s-%s-%s' % (self.sensor_id, str(self.trip_id),
                             str(self.timestamp))

    class Meta:

        ordering = ['-added']
