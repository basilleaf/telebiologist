# How to Post Data

do something like:

    curl --data "t=124563&devID=18&tripID=3&n1=4&v1=9"  http://powerful-sands-3128.herokuapp.com/[SUPER SECRET URL PATH]

can accept up to 3 more key/value pairs with each POST:

    n2=v2,n3=v3,n4=v4



# How to Get the Data

<http://powerful-sands-3128.herokuapp.com/>

that is default paginated, so like:

<http://powerful-sands-3128.herokuapp.com?page=2>

to turn pagination off and get all the data, say page=all

<http://powerful-sands-3128.herokuapp.com?page=all>

also can get csv format:

<http://powerful-sands-3128.herokuapp.com?page=2&fmt=csv>


