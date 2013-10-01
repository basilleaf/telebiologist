import os
from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from server.views import sensordata
from server.api import ReadingResource

reading_resource = ReadingResource()

SUPER_SECRET_URL_PATH = os.environ['SUPER_SECRET_URL_PATH']

urlpatterns = patterns('',
    # Examples:
    (r'^api/', include(reading_resource.urls)),
    (r'^' + SUPER_SECRET_URL_PATH + '$', csrf_exempt(sensordata.as_view())),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
