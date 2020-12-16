from soundControls import mute_unmute
from times_processing import get_prayer_times
from api_requests import send_request_console
from check import check_prayer_now, check_date
from time import sleep
import datetime


def main():
    today = None
    prayer_times = {}
    while True:
        if check_prayer_now(prayer_times):
            mute_unmute(300)
        if not check_date(today):
            today = datetime.datetime.now().date()
            request = send_request_console()
            prayer_times = get_prayer_times(request['data']['timings'])

            # Printing Date and Prayer times for the user
            print(''.join(['=' for i in range(20)]))
            print(f'Date: {today}')
            print(''.join(['-' for i in range(len(str(today))+6)]))
            print('Prayer Times: ')
            print(''.join(['-' for i in range(len('Prayer Times: '))]))
            for i, j in prayer_times.items():
                print('{}: {}'.format(i, str(j)))
        sleep(15)


if __name__ == "__main__":
    main()
