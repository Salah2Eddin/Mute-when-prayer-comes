from sound import Sound
import requests
import sched
import time
import datetime
import ipinfo
import socket
# current time variables
today = datetime.date.today


def getLoc():
    token = 'd11008b70e61d8'
    handler = ipinfo.getHandler(token)
    return handler.getDetails()


# get prayers times from online api
def apiRequest():
    locationData = getLoc()
    zone = locationData.timezone
    latitude = locationData.latitude
    longitude = locationData.longitude

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


def muteAndUnmute(delay):
    # using a fake keypress on your keyboard mute button
    # we will mute and unmute your volume
    Sound.mute()
    time.sleep(delay)
    Sound.mute()


def getTime():
    # replaced secs and microsecs to make it a bit more precise
    return datetime.datetime.now().time().replace(second=0, microsecond=0)


def getPrayersTimes(data):
    # Get the time strings
    prayersTimesMap = data['data']['timings']
    prayersTimes = []

    # Turn the strings into Time Objects !!
    for prayer in prayersTimesMap:
        prayerTimeString = prayersTimesMap[prayer]
        prayerTimeStringList = prayerTimeString.split(':')
        prayerTimeList = [int(i) for i in prayerTimeStringList]
        prayerTime = datetime.time(prayerTimeList[0], prayerTimeList[1])
        prayersTimes.append(prayerTime)
    return prayersTimes


data = apiRequest()
print(data)


def checkForTime():
    global today, data
    prayersTimes = getPrayersTimes(data)
    now = getTime()
    # if there is a prayer now
    if now in prayersTimes:
        print('mute')
        muteAndUnmute(300)
        print('unmute')
    # if todayVariable is not today (Day ended and we are in next day)
    elif today != datetime.date.today:
        today = datetime.date.today  # Make it next day
        data = apiRequest()  # Also get the new prayers time


schedualer = sched.scheduler(time.time, time.sleep)
schedualer.enter(60, 1, checkForTime)
print("""
Running\n
This script will mute your computer while there is a prayer\n
It will check for time every minute and will mute your computer for 5 minutes\n
To quit use ctrl+c""")

while True:
    schedualer.run()
