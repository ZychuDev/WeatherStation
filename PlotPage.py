import tkinter as tk
import datetime
import time 
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Database import read_measurements



class PlotPage(tk.Frame):
    name = "Plot"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.contoller = controller
        self.width = 2
        self.height = 4

        self.x_data = [1, 2, 3, 4, 5]
        self.y_data = [1, 2, 3, 4, 5]
        self.y_axes = 'pressure'

        self.f = Figure(figsize=(10,5), dpi=100)

        self.ax = self.f.add_subplot(111)

        label = ttk.Label(self, text="Measurements Visualization", font=18, justify="center")
        label.pack(side="top", pady=10, padx=10)

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.get_tk_widget().pack(side="top",fill='both',expand=True)

        n = tk.StringVar()
        self.y_picker = ttk.Combobox(self, width = 15, textvariable = n)
        self.y_picker.bind('<<ComboboxSelected>>', self.y_picked)
        
        # Adding combobox drop down list
        self.y_picker['values'] = ('pressure', 'PM2_5', 'PM10', 'temperature')
        
        self.y_picker.pack(side="top",fill='both',expand=True)
  
        # Shows february as a default value
        self.y_picker.current(1) 

        buttonMenu = ttk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("Main"))
        buttonMenu.pack(side="top",fill='both',expand=True)

        buttonDelete = ttk.Button(self, text="Show Table", command=lambda: controller.show_frame("Second"))
        buttonDelete.pack(side="top",fill='both',expand=True)
   

    def y_picked(self, event):
        self.y_axes = self.y_picker.get()
        self.draw_plot()

    def draw_plot(self):
        print("Ploting",self.y_axes )
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, "o", picker=15)
        self.ax.title.set_text(self.y_axes)
        cid = self.f.canvas.mpl_connect('pick_event', self.on_click)
        self.canvas.draw()

    def check_updates(self, controller):

        t = time.time()
        print(t)
        today = datetime.datetime.now()

        last_week = today + datetime.timedelta(days=100000)
        today = datetime.datetime.timestamp(today)
        last_week = datetime.datetime.timestamp(last_week)
        print(today)
        print(last_week)
        measurements = read_measurements(0 ,today)

        self.x_data = [m['timestamp'] for m in measurements]
        self.y_data = [m[self.y_axes] for m in measurements]

        self.draw_plot()
        controller.update_event = self.after(10000, lambda: self.check_updates(controller))


    def on_click(self):
        pass
    
    def delete(self):
        pass
