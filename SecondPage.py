from os import read
import tkinter as tk
import time 
from tkinter import ttk
from Table import Table
from Database import read_measurements
LARGE_FONT = 18

class SecondPage(tk.Frame):
    name = "Second"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        label = ttk.Label(self, text="Measurements", font=LARGE_FONT, justify="center")
        label.pack(side="top", pady=10, padx=10)

        self.t = Table(self, 30,5)
        self.t.pack(side="top", fill="x")
        
        self.t.set(0,0,"Timestamp")
        self.t.set(0,1,"PM2_5")
        self.t.set(0,2,"PM10")
        self.t.set(0,3,"Pressure")
        self.t.set(0,4,"Temperature")

        button = ttk.Button(self, text="Update Table", command=self.update_table)
        button.pack(side="top", fill="both",expand=True)

        button1 = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("Main"))
        button1.pack(side="top", fill="both",expand=True)

        button2 = ttk.Button(self, text="Show Plot", command=lambda: controller.show_frame("Plot"))
        button2.pack(side="top", fill="both",expand=True)

        self.update_table()
    def update_table(self):
        measurements = read_measurements(0, time.time())
        last_measurements= measurements[-29:]

        for i, m in enumerate(last_measurements):
            self.t.set(i+1, 0, m['timestamp'])
            self.t.set(i+1, 1, m["PM2_5"])
            self.t.set(i+1, 2, m["PM10"])
            self.t.set(i+1, 3, m["pressure"])
            self.t.set(i+1, 4, m["temperature"])
    




    def check_updates(self, controller):
        #print("Table writing")
        controller.update_event = self.after(10, lambda: self.check_updates(controller))