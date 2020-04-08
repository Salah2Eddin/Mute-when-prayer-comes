from soundControls import mute, unmute
import requests
import time
import datetime
import sys
# current day variables
today = datetime.date.today


# get prayers times from online api
def apiRequest():
    # Times API call and params
    # To get prayer times
    URL = 'http://api.aladhan.com/v1/timingsByCity'
    PARAMS = {'city': 'cairo', 'country': 'egypt', 'method': 5}
    r = requests.get(url=URL, params=PARAMS)
    return r.json()


def muteAndUnmute(delay):
    # Mute and after delay unmute
    mute()
    time.sleep(delay)
    unmute()


def getTime():
    # replaced secs and microsecs with 0
    time12h = datetime.datetime.now().time()
    time12h = time12h.replace(second=0, microsecond=0).strftime('%I:%M %p')
    time12h = datetime.datetime.strptime(time12h, '%I:%M %p').time()
    return time12h


def getPrayersTimes(data):
    # Get the time strings
    prayersTimesMap = data['data']['timings']
    prayersTimes = []

    # Turn the strings into DateTime objects
    for prayer in prayersTimesMap:
        prayerTime24H = datetime.datetime.strptime(prayersTimesMap[prayer],
                                                   '%H:%M')
        prayerTimeStr = prayerTime24H.strftime('%I:%M %p')
        prayerTime = datetime.datetime.strptime(prayerTimeStr, '%I:%M %p')
        prayersTimes.append(prayerTime.time())
    return prayersTimes


# check for internet
# by sending a request to our api
try:
    data = apiRequest()
except requests.exceptions.ConnectionError:
    print('No internet connection , Reconnect than run the scirpt')
    sys.exit()

prayersTimes = getPrayersTimes(data)


def checkForTime():
    global today, data, prayersTimes
    now = getTime()
    # if there is a prayer now
    if now in prayersTimes:
        print('mute')
        muteAndUnmute(300)
        print('unmute')
    # if todayVariable is not today (Day ended and we are in next day)
    elif today != datetime.date.today():
        today = datetime.date.today()  # Make it next day
        # Also get the new prayers time
        data = apiRequest()
        prayersTimes = getPrayersTimes(data)


print("""
Running\n
This script will mute your computer while there is a prayer\n
It will check for time every minute and will mute your computer for 5 minutes\n
To quit use ctrl+c""")

while True:
    checkForTime()
    time.sleep(30)
