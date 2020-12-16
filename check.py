from times_processing import *
import datetime


def check_prayer_now(prayerTimes):
    """
    checks if there is a prayer now\n
    params:
        prayerTimes (dict): dict with all prayer times as datatime.time objects
    return:
        True: There is a prayer now
        False: There isn't a prayer now
    """
    now = get_time()
    if now in prayerTimes.values():
        return True
    else:
        return False


def check_date(recorded_date):
    """
    checks if given date is today\n
    params:
        recorded_date(datetime.date): date to check
    return:
        True: given date is today
        False: given date is not today
    """
    if datetime.datetime.now().date() == recorded_date:
        return True
    else:
        return False
