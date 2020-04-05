from sound import Sound
import requests
import time
import datetime
import sys
# current time variables
today = datetime.date.today


# get prayers times from online api
def apiRequest():
    # Times API call and params
    URL = 'http://api.aladhan.com/v1/timingsByCity'
    PARAMS = {'city': 'cairo', 'country': 'egypt', 'method': 5}
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
        prayerTime24H = datetime.datetime.strptime(prayersTimesMap[prayer],
                                                   '%H:%M')
        prayerTimeStr = prayerTime24Form.strftime('%I:%M')
        prayerTime = datetime.datetime.strptime(prayerTime12FormStr, '%I:%M')
        prayersTimes.append(prayerTime.time())
    return prayersTimes


try:
    apiRequest()
except requests.exceptions.ConnectionError:
    print('No internet connection , Reconnect than run the scirpt')
    sys.exit()


data = apiRequest()
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
    elif today != datetime.date.today:
        today = datetime.date.today  # Make it next day
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
