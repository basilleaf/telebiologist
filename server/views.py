from django.views.generic.base import View
from django.http import HttpResponse
import json
from django.core import serializers
from server.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

class testview(View):

    def get(self, request):
        data = Reading.objects.all()
        paginator = Paginator(data, 100)
        page = request.GET.get('page')
        try:
            page_data = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_data = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_data = paginator.page(paginator.num_pages)

        jsondata = serializers.serialize('json', page_data)
        return HttpResponse(jsondata, mimetype='application/json')


class dataview(View):

    def get(self, request):
        # return HttpResponse('hello world')
        data = Reading.objects.all()
        jsondata = serializers.serialize('json', data)
        return HttpResponse(jsondata, mimetype='application/json')

class sensordata(View):

    def post(self, request):
        timestamp = request.POST.get('t', None)
        device_id = request.POST.get('devID', None)
        trip_id = request.POST.get('tripID', None)
        sensor_id = request.POST.get('n1', None)
        sensor_value = request.POST.get('v1', None)

        reading = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id, sensor_value=sensor_value)
        reading.save()

        # are there more sensors on this thing?
        sensor_id2 = request.POST.get('n2', None)
        sensor_value2 = request.POST.get('v2', None)
        if sensor_id2:
            reading2 = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id2, sensor_value=sensor_value2)
            reading2.save()

        # i know i am so lame
        sensor_id3 = request.POST.get('n3', None)
        sensor_value3 = request.POST.get('v3', None)
        if sensor_id3:
            reading3 = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id3, sensor_value=sensor_value3)
            reading3.save()

        # so so so so lame
        sensor_id4 = request.POST.get('n4', None)
        sensor_value4 = request.POST.get('v4', None)
        if sensor_id4:
            reading4 = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id4, sensor_value=sensor_value4)
            reading4.save()

        return HttpResponse('ok')
