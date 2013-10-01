#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from tastypie.resources import ModelResource, ALL
from serializers import CSVSerializer
from .models import Reading

class ReadingResource(ModelResource):
    class Meta:
        queryset = Reading.objects.all()
        resource_name = 'readings'
        filtering = {
            'timestamp': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'device_id': ALL,
            'trip_id': ALL,
            'sensor_id': ALL,
            'sensor_value': ALL,
            'added': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        serializer = CSVSerializer(formats=['json', 'jsonp', 'csv', 'xml', 'yaml', 'html', 'plist'])




