import tkinter as tk


class LabelsTable(tk.Frame):
    def __init__(self, parent, items_dict={}):
        tk.Frame.__init__(self, parent)
        self.items_dict = items_dict
        self.set_dict(self.items_dict)

    def clear_children(self):
        for child in self.winfo_children():
            child.destroy()

    def set_dict(self, new_dict):
        self.clear_children()
        self.items_dict = new_dict
        self.labels_grid = [
            (tk.Label(self, text=i), tk.Label(self, text=j))
            for i, j in new_dict.items()]
        for i in range(len(self.labels_grid)):
            header = self.labels_grid[i][0]
            header.grid(column=i, row=0)
            value = self.labels_grid[i][1]
            value.grid(column=i, row=1)
