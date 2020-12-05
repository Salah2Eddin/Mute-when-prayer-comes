from soundControls import mute_unmute
from get_times import get_prayer_times
from api_requests import prayersAPI_request, get_loc
from check import check_prayer_now, check_date
from time import sleep
import requests
import datetime
import urllib3
import sys


def send_request():
    i = 0
    while i < 3:
        try:
            loc_data = get_loc()
            return prayersAPI_request(loc_data)
        except (requests.exceptions.ConnectionError or
                urllib3.exceptions.ReadTimeoutError):
            if i == 2:
                print('No internet connection , Reconnect than run the scirpt')
                sys.exit()
            else:
                print('Failed to connect to the api.. try:{}'.format(i+1))
                i += 1
                continue


def main():
    today = datetime.datetime.now().date()

    request = send_request()
    prayer_times = get_prayer_times(request['data']['timings'])

    print(f'Date: {today}')
    print(prayer_times)

    while True:
        if check_prayer_now(prayer_times):
            mute_unmute(300)
        if not check_date(today):
            today = datetime.datetime.now().date()
            request = send_request()
            prayer_times = get_prayer_times(request['data']['timings'])
            print(f'Date: {today}')
            print(prayer_times)
        sleep(15)


if __name__ == "__main__":
    main()
