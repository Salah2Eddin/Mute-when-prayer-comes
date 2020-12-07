from soundControls import mute_unmute
from get_times import get_prayer_times
from api_requests import send_request
from check import check_prayer_now, check_date
from time import sleep
import tkinter as tk
import datetime
today = None
prayer_times = {}


class PrayersTable(tk.Frame):
    def __init__(self, parent, prayers_dict):
        tk.Frame.__init__(self, parent)
        self.prayers_dict = prayers_dict
        self.labels = [
            (tk.Label(self, text=i), tk.Label(self, text=j))
            for i, j in prayers_dict.items()]
        for i in range(len(self.labels)):
            label = self.labels[i][0]
            label.grid(column=i, row=0)
            label = self.labels[i][1]
            label.grid(column=i, row=1)

    def set_dict(self, new_dict):
        self.prayers_dict = new_dict
        self.labels = [
            (tk.Label(self, text=i), tk.Label(self, text=j))
            for i, j in new_dict.items()]
        for i in range(len(self.labels)):
            label = self.labels[i][0]
            label.grid(column=i, row=0)
            label = self.labels[i][1]
            label.grid(column=i, row=1)


class TimeLabel(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.time = datetime.datetime.now().time()
        self.time_str = self.time.strftime('%I:%M:%S %p')
        self.time_label = tk.Label(self, text=self.time_str)
        self.time_label.grid(column=0, row=0)
        self.after(s2ms(1), self.set_time)

    def set_time(self):
        self.time = datetime.datetime.now().time()
        self.time_str = self.time.strftime('%I:%M:%S %p')
        self.time_label.configure(text=self.time_str)
        self.time_label.grid(column=0, row=0)
        self.after(s2ms(1), self.set_time)


def s2ms(sec):
    """
    Turns Seconds into MicroSeconds
    """
    return sec*1000


def check():
    global today, prayer_times
    if check_prayer_now(prayer_times):
        mute_unmute(300)
    if not check_date(today):
        today = datetime.datetime.now().date()
        request = send_request()
        prayer_times = get_prayer_times(request['data']['timings'])
        date.configure(text='Date: {}'.format(datetime.datetime.now().date()))
        table.set_dict(prayer_times)
        window.after(s2ms(15), check)


window = tk.Tk()
window.title("Mute when prayer comes")
window.geometry('360x400')
date = tk.Label(window, text='Date: {}'.format(''))
date.grid(column=0, row=0)
time = TimeLabel(window)
time.grid(column=1, row=0)
table = PrayersTable(window, {})
table.grid(column=0, row=1)

if __name__ == '__main__':
    print('Started main loop')
    window.after(1, check)
    window.mainloop()
