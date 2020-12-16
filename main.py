from soundControls import mute_unmute
from times_processing import get_prayer_times
from api_requests import send_request
from check import check_prayer_now, check_date
from widgets.TimeLabel import TimeLabel
from widgets.LabelsTable import LabelsTable
from time import sleep
import tkinter as tk
import datetime
today = None
prayer_times = {}


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mute when prayer comes")
        self.resizable(0, 0)

        self.date = tk.Label(self,
                             text='Date: {}'.format(''))
        self.date.grid(column=0, row=0, sticky=tk.W)

        self.time = TimeLabel(self)
        self.time.grid(column=1, row=0, sticky=tk.E, padx=4)

        self.table = LabelsTable(self)
        self.table.grid(column=0, row=1, columnspan=2, padx=4)

        self.btn = tk.Button(self, command=self.reload, text='Reload times')
        self.btn.grid(column=0, row=2, sticky=tk.NE, columnspan=2, padx=4,
                      pady=2)

    def check(self):
        global today, prayer_times
        if check_prayer_now(prayer_times):
            mute_unmute(300)
        if not check_date(today):
            today = datetime.datetime.now().date()
            self.reload()
            self.after(15*1000, self.check)

    def reload(self):
        global prayer_times
        self.table.set_dict({'Fetching Times': 'Fetching Times'})
        request = send_request()
        if request:
            timings = request['data']['timings']
            prayer_times = get_prayer_times(timings)
            self.date.configure(text='Date: {}'.format(today))
            self.table.set_dict(prayer_times)
        elif request is None:
            if prayer_times is not {}:
                err_msg = "Failed to fetch times.. please reload"
                self.table.set_dict({err_msg: err_msg})
            else:
                tk.messagebox.showinfo(
                    title="Error", message=err_msg)


if __name__ == '__main__':
    window = App()
    window.reload()
    print('Started main loop')
    window.after(1000, window.check)
    window.mainloop()
