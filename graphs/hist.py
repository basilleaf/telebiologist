import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json
import urllib2


url = 'http://powerful-sands-3128.herokuapp.com?page=all'
json.loads(requests.get(url)
f = urllib2.urlopen(url)
json = json.load(f)