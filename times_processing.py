import datetime


def get_time():
    """
    Gets current time object than return it without seconds\n
    params:
        none
    return:
        time: current time without seconds and microseconds
    """
    time = datetime.datetime.now().time()
    time = time.replace(second=0, microsecond=0)
    return time


def get_prayer_times(prayers_dict, ignore_extra=True):
    """
    Turns prayer times in dict into datetime.time objects\n
    params:
        prayers_dict (dict): dict with all prayers you got from your api
            It must include ["fajr","dhuhr","asr","maghrib","isha"]
            Times must be a string in 24h form.
        ignore_extra (bool): Default=True
            True: Ignore any extra prayers in the prayers dict
            False: Don't ignore anything in the prayers dict
    return:
        prayer_times (dict): prayers as str and times as datetime.time objects
    """
    prayers_times = {}
    prayers = ["fajr", "dhuhr", "asr", "maghrib", "isha"]
    for prayer in prayers_dict:
        if (prayer.lower() not in prayers and ignore_extra is True):
            continue
        prayers_times[prayer] = datetime.datetime.strptime(
            prayers_dict[prayer], '%H:%M').time()
    return prayers_times
