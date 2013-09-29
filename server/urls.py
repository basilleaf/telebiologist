from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from server.views import sensordata
from django.views.decorators.csrf import csrf_exempt
from secrets import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', csrf_exempt(sensordata.as_view())),
    url(r'^' + super_secret_url_path + '$', csrf_exempt(sensordata.as_view())),
    # url(r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
