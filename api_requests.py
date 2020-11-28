from soundControls import mute_unmute
import requests
import time
import datetime
import ipinfo
import socket
import sys


def get_loc():
    """
    Send your ip address to "ipinfo api" than
    get some location data from it\n
    returns dict with timezone as 'zone', longitude as 'long', and latitude as
    'lat'
    """
    token = 'd11008b70e61d8'
    handler = ipinfo.getHandler(token)
    data = handler.getDetails()
    return {"zone": data.timezone,
            "long": data.longitude,
            "lat": data.latitude}


# get prayer times from online api
def prayersAPI_request(locData):
    """
    locData -> dict: your location data in the form of\n
    {
        "zone": timezone,\n
        "long": longitude,\n
        "lat": latitude\n
    }\n
    send request to 'aladhan.com' timestamp api with your timezone to get a
    timestamp\n
    than send request to their prayer times api and return respose as json
    """

    zone = locData['zone']
    longitude = locData['long']
    latitude = locData['lat']

    # timestamp API call and params
    URL = f'http://api.aladhan.com/v1/currentTimestamp'
    PARAMS = {'zone': zone}
    r = requests.get(url=URL, params=PARAMS)
    timestamp = r.json()['data']

    # Times API call and params
    URL = f'http://api.aladhan.com/v1/timings/$timestamp'
    PARAMS = {'latitude': latitude,
              'longitude': longitude,
              'method': 5}
    r = requests.get(url=URL, params=PARAMS)
    return r.json()
