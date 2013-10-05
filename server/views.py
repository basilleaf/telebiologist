#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from django.views.generic.base import View
from django.http import HttpResponse
from django.core import serializers
from server.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict

class sensordata(View):
    # takes POST submissions of sensor data and saves to db

    def post(self, request):

        # supporting standard field names as they appear in the model
        timestamp = request.POST.get('timestamp, None)
        device_id = request.POST.get('device_id', None)
        trip_id = request.POST.get('trip_id', None)
        sensor_id = request.POST.get('sensor_id', None)
        sensor_value = request.POST.get('sensor_value', None)

        # this is just to support Jethro's original Science Hack Day code..
        if not sensor_id:
            timestamp = request.POST.get('t', None)
            device_id = request.POST.get('devID', None)
            trip_id = request.POST.get('tripID', None)
            sensor_id = request.POST.get('n1', None)
            sensor_value = request.POST.get('v1', None)

        reading = Reading(timestamp=timestamp, device_id=device_id,
                          trip_id=trip_id, sensor_id=sensor_id,
                          sensor_value=sensor_value)
        reading.save()

        # are there more sensors on this thing?

        sensor_id2 = request.POST.get('n2', None)
        sensor_value2 = request.POST.get('v2', None)
        if sensor_id2:
            reading2 = Reading(timestamp=timestamp,
                               device_id=device_id, trip_id=trip_id,
                               sensor_id=sensor_id2,
                               sensor_value=sensor_value2)
            reading2.save()

        # i know i am so lame

        sensor_id3 = request.POST.get('n3', None)
        sensor_value3 = request.POST.get('v3', None)
        if sensor_id3:
            reading3 = Reading(timestamp=timestamp,
                               device_id=device_id, trip_id=trip_id,
                               sensor_id=sensor_id3,
                               sensor_value=sensor_value3)
            reading3.save()

        # so so so so lame

        sensor_id4 = request.POST.get('n4', None)
        sensor_value4 = request.POST.get('v4', None)
        if sensor_id4:
            reading4 = Reading(timestamp=timestamp,
                               device_id=device_id, trip_id=trip_id,
                               sensor_id=sensor_id4,
                               sensor_value=sensor_value4)
            reading4.save()

        return HttpResponse('ok')

