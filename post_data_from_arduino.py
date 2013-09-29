import serial
import urllib
import urllib2

url = 'http://powerful-sands-3128.herokuapp.com/sciencehackday2014fromthefuture'

ser = serial.Serial('/dev/tty.usbmodemfa131', 19200)
while True:
    data = ser.readline()
    try:
        (reading, time) = data.split(';')
        (n1, v1) = reading.split(':')
        v1 = int(v1)
        t = int(time.split(':')[1])
        tripID = 3
        devID = 3
        payload = {'t':t,  'n1': n1, 'v1': v1, 'tripID': tripID, 'devID': devID}
        payload_encoded = urllib.urlencode(payload)
        urllib2.urlopen(url, payload_encoded)
        print 'ok: ' + str(payload)
    except:
        print 'nope'
        pass

