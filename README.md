This app accepts sensor data (or any data) via http POST requests and exposes an api to fetch the data

The script post_data_from_arduino.py takes readings from serial port and posts to this app.

## How to Post Data

do something like:

    curl --data "t=124563&devID=18&tripID=3&n1=4&v1=9"  http://powerful-sands-3128.herokuapp.com/[SUPER_SECRET_URL_PATH]

can accept up to 3 more key/value pairs with each POST:

    n2=v2,n3=v3,n4=v4



## How to Get Data from the API

latest readings are here:

<http://powerful-sands-3128.herokuapp.com/api/readings?format=json>

you can filter by any field, for example sensor_id:

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&sensor_id=lux>

and you can search by date added and timestamp in different ways: ['exact', 'range', 'gt', 'gte', 'lt', 'lte'] For example, here are all readings of sensor "lux" added on a specific day

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&offset=100&sensor_id=lux&limit=0&added__gte=2013-09-29>

results are paginated, default limit per page is 20, in the meta of the first page you can grab the link to the next/previous page, or set the offset yourself, like:

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&offset=100>

also you can override the default limit

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&limit=100>

If you want to skip paginating and grab all the data, set limit=0

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&limit=0>

you can also get csv, for example this will grab all lux readings on a given day as csv:

<http://powerful-sands-3128.herokuapp.com/api/readings/?format=json&sensor_id=lux&limit=0&added__gte=2013-09-2&format=csv>
