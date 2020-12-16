from soundControls import mute_unmute
from time import sleep
import requests
import urllib3
import datetime
import ipinfo
import socket
import sys


def get_loc():
    """
    Send your ip address to "ipinfo api" and get some location data from it
    params:
        none
    return:
        dict: timezone as 'zone', longitude as 'long', and latitude as 'lat'
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
    sends a request to 'aladhan.com' timestamp api with your timezone to get a
    timestamp than sends a request to their prayer times api
    params:
        locData (dict): your location data in the following form
        {"zone": timezone, "long": longitude, "lat": latitude}
    return:
        response (json): the response of the api
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


def send_request_console():
    """
    the function used by console script to send requests
    params:
        none
    return:
        response: the response from sending all the required requests
    """
    for i in range(0, 3):
        try:
            loc_data = get_loc()
            response = prayersAPI_request(loc_data)
            return response
        except (requests.exceptions.ConnectionError or
                requests.exceptions.ReadTimeout or
                urllib3.exceptions.ReadTimeoutError):
            if i == 2:
                print('Failed to connect to the api after 3 tries..')
                print('Check your internet connection')
                sys.exit()
            else:
                print('Failed to connect to the api.. try:{}'.format(i+1))
                sleep(1)
                for i in range(0, 3):
                    print('Trying to reconnect in {}..'.format(3-i))
                    sleep(1)
                    continue


def send_request():
    """
    the function used by windows application to send requests
    params:
        none
    return:
        response: the response from sending all the required requests
    """
    for i in range(0, 3):
        try:
            loc_data = get_loc()
            response = prayersAPI_request(loc_data)
            return response
        except (requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout,
                urllib3.exceptions.ReadTimeoutError):
            if i == 2:
                return None
            else:
                sleep(3)
