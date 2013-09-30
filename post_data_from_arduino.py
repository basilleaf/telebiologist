#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
import urllib
import urllib2
from secrets import *

url = 'http://powerful-sands-3128.herokuapp.com/' \
    + SUPER_SECRET_URL_PATH

ser = serial.Serial('/dev/tty.usbmodemfa131', 19200)
while True:
    data = ser.readline()
    try:
        (reading, time) = data.split(';')
        (n1, v1) = reading.split(':')
        v1 = int(v1)
        t = int(time.split(':')[1])
        tripID = 4
        devID = 3
        payload = {
            't': t,
            'n1': n1,
            'v1': v1,
            'tripID': tripID,
            'devID': devID,
            }
        payload_encoded = urllib.urlencode(payload)
        urllib2.urlopen(url, payload_encoded)
        print 'ok: ' + str(payload)
    except:
        print 'nope'  # i am a horrible coder
        pass
