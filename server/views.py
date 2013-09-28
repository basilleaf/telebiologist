from django.views.generic.base import View
from django.http import HttpResponse
import json
from django.core import serializers
from .models import *

class sensordata(View):

    def get(self, request):
        # return HttpResponse('hello world')
        data = Reading.objects.all()
        jsondata = serializers.serialize('json', data)
        return HttpReponse(jsondata, mimetype='application/json')

    def post(self, request):
        timestamp = request.GET.get('t', None)
        device_id = request.GET.get('devID', None)
        trip_id = request.GET.get('tripID', None)
        sensor_id = request.GET.get('n1', None)
        sensor_value = request.GET.get('v1', None)

        reading = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id, sensor_value=sensor_value)
        reading.save()
