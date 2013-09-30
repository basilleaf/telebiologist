#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.http import HttpResponse
import json
from django.core import serializers
from server.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict


class testview(View):
    # this is a stupid view to test new versions of dataview
    # because I don't haz this deployed locally and need place to test #oops
    def get(self, request):
        return HttpResponse('hello test')


class dataview(View):
    # ways to view the data that has been uploaded..
    # an api of sorts..

    def get(self, request):
        page = request.GET.get('page')
        fmt = request.GET.get('fmt', 'json')
        page_data = self.get_page_data(page)

        # json serializer doesn't play nice with paginator and that is stupid, thus:

        if fmt == 'json':
            json_struct = []
            for p in page_data:
                json_dict = model_to_dict(p)
                json_dict['added'] = str(p.added)  # have to add timestamp manually because model_to_dict is a dick.
                json_struct.append(json_dict)  # append this dict to the larger struct

            # jsondata = serializers.serialize('json', json_struct)

            return HttpResponse(json.dumps(json_struct),
                                mimetype='application/json')

        if fmt == 'csv':
            csv_struct = []
            for p in page_data:
                this_dict = model_to_dict(p)
                this_dict['added'] = str(p.added)  # again with the asshole model_to_dict
                for (k, v) in this_dict.iteritems():
                    csv_struct.append('"' + '","'.join([str(v) for (k,
                            v) in this_dict.iteritems()]) + '"')

            # insert column labels in first row

            csv_struct.insert(0, '"' + '","'.join([str(k) for (k, v) in
                              this_dict.iteritems()]) + '"')

            # jsondata = serializers.serialize('json', json_struct)

            return HttpResponse('\n'.join(csv_struct),
                                mimetype='text/csv')

    def get_page_data(self, page):
        # this sorts out pagination of the requested data (whywat)

        data = Reading.objects.all()
        if page == 'all':
            return data

        paginator = Paginator(data, 20)

        try:
            page_data = paginator.page(page)
        except PageNotAnInteger:

            # If page is not an integer, deliver first page.

            page_data = paginator.page(1)
        except EmptyPage:

            # If page is out of range (e.g. 9999), deliver last page of results.

            page_data = paginator.page(paginator.num_pages)

        return page_data


class sensordata(View):
    # takes POST submissions of sensor data and saves to db

    def post(self, request):
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
