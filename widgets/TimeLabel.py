import tkinter as tk
import datetime


class TimeLabel(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.time = datetime.datetime.now().time()
        self.time_label = tk.Label(self)
        self.set_time()

    def set_time(self):
        self.time = datetime.datetime.now().time()
        self.time_str = self.time.strftime('%I:%M:%S %p')
        self.time_label.configure(text=self.time_str)
        self.time_label.grid(column=0, row=0)
        self.after(1000, self.set_time)
