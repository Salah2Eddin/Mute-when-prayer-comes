import datetime

"""
All time processing functions are here
"""


def get_time() -> datetime.time:
    """
    Get current time object than replace seconds and microseconds with zeros \n
    return datetime.time object
    """
    time = datetime.datetime.now().time()
    time = time.replace(second=0, microsecond=0).strftime('%I:%M %p')
    time = datetime.datetime.strptime(time, '%I:%M %p').time()
    return time


def get_prayer_times(prayers_dict, ignore_extra=True) -> datetime.time:
    """
    prayers_dict: dict with all prayers you got from your api
    It must include ["Fajr","Dhuhr","Asr","Maghrib","Isha"] case sensitive keys
    Times must be in 24h form as a string.
    Example dict :{'Asr':'02:45','Maghrib':'04:32'}\n
    ignore_extra default=True:\n
    True: Ignore any extra prayers in the prayers dict\n
    False: Don't ignore anything in the prayers dict\n
    """
    prayers_times = {}

    # Turn the strings dict into datetime.time dict
    for prayer in prayers_dict:
        if (prayer not in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"] and
           ignore_extra is True):
            continue

        prayer_time_24H = datetime.datetime.strptime(prayers_dict[prayer],
                                                     '%H:%M')
        prayer_time_str = prayer_time_24H.strftime('%I:%M %p')
        prayer_time = datetime.datetime.strptime(prayer_time_str, '%I:%M %p')
        prayers_times[prayer] = prayers_times.time()

    return prayers_times
