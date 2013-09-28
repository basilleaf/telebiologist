class sensordata(View):

    def get(self, request):



    def post(self, request):
        timestamp = request.GET.get('t', None)
        device_id = request.GET.get('devID', None)
        trip_id = request.GET.get('tripID', None)
        sensor_id = request.GET.get('n1', None)
        sensor_value = request.GET.get('v1', None)

        reading = Reading(timestamp=timestamp, device_id=device_id, trip_id=trip_id, sensor_id=sensor_id, sensor_value=sensor_value)
        reading.save()
