from sound import Sound
import requests
import sched
import time
import datetime

# current time variables
today = datetime.date.today


# get prayers times from online api
def apiRequest():
    # API params
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


def getPrayersTimes():
    # Get the time strings
    prayersTimesMap = data['data']['timings']
    prayersTimes = []

    # Turn the strins into Time Objects !!
    for prayer in prayersTimesMap:
        prayerTimeString = prayersTimesMap[prayer]
        prayerTimeStringList = prayerTimeString.split(':')
        prayerTimeList = [int(i) for i in prayerTimeStringList]
        prayerTime = datetime.time(prayerTimeList[0], prayerTimeList[1])
        prayersTimes.append(prayerTime)
    return prayersTimes


data = apiRequest()


def checkForTime():
    global today, data
    prayersTimes = getPrayersTimes()
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
