from django.views.generic.base import View
from django.http import HttpResponse
import json
from django.core import serializers
from server.models import *
from django.views.decorators.csrf import csrf_exempt


class sensordata(View):

    def get(self, request):
        # return HttpResponse('hello world')
        data = Reading.objects.all()
        jsondata = serializers.serialize('json', data)
        return HttpResponse(jsondata, mimetype='application/json')

    def post(self, request):
        timestamp = request.POST.get('t', None)
        device_id = request.POST.get('devID', None)
        trip_id = request.POST.get('tripID', None)
        sensor_id = request.POST.get('n1', None)
        sensor_value = request.POST.get('v1', None)

        reading = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id, sensor_value=sensor_value)
        reading.save()

        return HttpResponse('ok')
