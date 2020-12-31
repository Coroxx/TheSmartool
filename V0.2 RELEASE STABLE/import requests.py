import requests
from urllib.request import urlopen
import urllib

try:
    urllib.urlopen(
        "http://google.com",
        proxies={'http':'188.166.245.245:8000'}
    )
except IOError:
    print ("Connection error! (Check proxy)")
else:
    print ("All was fine")

