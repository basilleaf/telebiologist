from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from server.views import sensordata, dataview, testview
from django.views.decorators.csrf import csrf_exempt
import os

SUPER_SECRET_URL_PATH = os.environ['SUPER_SECRET_URL_PATH']

urlpatterns = patterns('',
    # Examples:
    url(r'^$', csrf_exempt(dataview.as_view())),
    url(r'^test$', csrf_exempt(testview.as_view())),
    url(r'^' + SUPER_SECRET_URL_PATH + '$', csrf_exempt(sensordata.as_view())),
    # url(r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
