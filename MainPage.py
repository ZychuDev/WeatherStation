import tkinter as tk
from tkinter import ttk
import Database
import time

LARGE_FONT = 18

class MainPage(tk.Frame):
    name = "Main"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller

        label = ttk.Label(self, text="Weather station", font=32)
        label.pack(side="top", pady=10, padx=10)

        button1 = ttk.Button(self, text="Show Table", command=lambda: controller.show_frame("Second"))
        button1.pack(side="top",fill='both',expand=True)

        button2 = ttk.Button(self, text="Show Plot", command=lambda: controller.show_frame("Plot"))
        button2.pack(side="top",fill='both',expand=True)

    def check_updates(self, controller):
        # print(Database.read_measurements(0,time.time()))
        controller.update_event = self.after(10000, lambda: self.check_updates(controller))