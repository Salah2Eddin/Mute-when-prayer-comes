from get_times import *
import datetime


def check_prayer_now(prayerTimes):
    """
    prayerTimes -> Dict: dict with all prayer times as datatime.time objects
    check if there is a prayer now
    """
    now = get_time()
    if now in prayerTimes.values():
        return True
    else:
        return False


def check_date(recorded_date):
    """
    recordedDate -> datetime.date
    checks if today is the last date the script recorded
    returns true if today is the last recorded date
    if not it returns false
    """
    if datetime.datetime.now().date() == recorded_date:
        return True
    else:
        return False
