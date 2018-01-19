#!/usr/bin/python

# KRAKEN
# Purpose: Kraken is a GUI intended to guide an inexperienced user through the process of a WiFi Crack.
#         So far, it can scan for target networks with Wash, and then if WPS is enabled, it can use 
#            Reaver to crack the network.
#         What I am currently working on is parsing the data returned from Wash and render it usable 
#            for Reaver based on a filter looking for if WPS Lock is enabled.
#         In the future, I plan to add elements from aircrack-ng and JohnTheRipper.
# Functions:
# Monitor Mode Enable    : enable
# Run WASH 	             : wash
# Parse WASH results     : sort
# Run Reaver 	         : reave
# Run Aircrack-ng Suite  : airmon, aireplay, airodump
# Run JohnTheRipper      : johnny
# Run wifite             : fite
# Monitor Mode Disable   : disable

import tkinter as tk	# GUI module
import os			    # Used for commands to the terminal
import sys              # Used for termination


# MAIN


class AIR(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (Disclaimer, Monitor, Wash, Target, Reaver):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Disclaimer")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# DISCLAIMER


class Disclaimer(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This program is intended as a research tool only.", width=50, height=25)
        label.pack()
        #self.controller = controller
        #canvas = tk.Canvas(self, width = 750, height = 422, bg = "blue")
        #canvas.pack(expand = True, fill = "both")
        #photo = runfile("photo.gif", wdir="C://Users//tyler//Desktop//AIR//SRC")
        #backgroundImage= tk.PhotoImage(file = photo)
        #canvas.create_image(1, 1, image = image, anchor = "nw")

        button = tk.Button(self, text="Accept & Continue", command=lambda: controller.show_frame("Monitor"))
        button.pack(expand = True, fill ="x")

        button1 = tk.Button(self, text="Quit", command=sys.exit)
        button1.pack(expand =True, fill ="x")

# MONITOR


class Monitor(tk.Frame):
    def __init__(self, parent, controller):
        def enable():
            code = os.system('airmon-ng check kill')
            if code == 0:
                os.system('airmon-ng start wlan0mon')
            print('Monitor Mode: ON')
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Please enable Monitor Mode to continue.", width=50, height=25)
        label.pack()

        button = tk.Button(self, text="ENABLE", command=lambda: controller.show_frame("Wash"))
        button.pack(expand=True, fill ="x")

        button1 = tk.Button(self, text="QUIT", command=sys.exit)
        button1.pack(expand=True, fill="x")
# WASH


class Wash(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller 

        label = tk.Label(self, text="Press WASH to scan for networks.", width=50, height=25)
        label.pack()

        button = tk.Button(self, text="WASH", command=lambda: controller.show_frame("Target"))
        button.pack(expand=True, fill = "x")

        button1 = tk.Button(self, text="QUIT", command=sys.exit)
        button1.pack(side="bottom", expand=True, fill = "x")

# TARGET


class Target(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        file = 'C:\\Users\\tyler\\Desktop\\AIR\\SRC\\KRAKEN\\test.txt'
        data = open(file, 'r')
        content = data.read()

        lines = content.split('\n')
        entry = content.split()

        label = {}
        checkbox = {}
        var = {}
        sel = {}

        heading = tk.Label(self, text=lines[0])
        heading.pack(side="top", padx=10)
        cont = tk.Button(self, text="CONTINUE", command=lambda: controller.show_frame("Reaver"))
        cont.pack(side="bottom", expand=False, fill="x")
        for x in range(2, len(lines)-1):
            var[x] = tk.IntVar()
            checkbox[x] = tk.Radiobutton(self, text=lines[x], variable=var[x], value=1)
            checkbox[x].pack(padx=10, pady=10)

# REAVER


class Reaver(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Reaver is used to exploit networks that utilize WPS.")
        label.pack()

        option = ["-m, MAC", "-e. ESSID", "-c, Channel", "-o, out-file", "-f, Fixed Channel", "-5, 5 GHz", "-v, Verbose", "-q, Quiet", "-i, Name of Interface", "-b, BSSID", "-p, Use specified PIN", "-h, Help"]
        opt = {}
        check = {}
        for x in range(12):
             opt[x] = tk.IntVar()
             check[x] = tk.Checkbutton(self, text=option[x], variable=opt[x]) 
             check[x].pack()
        button1 = tk.Button(self, text="QUIT", command=sys.exit)
        button1.pack(side="bottom", fill="both")
        button = tk.Button(self, text="REAVER", command=sys.exit)
        button.pack(side="bottom", fill="both")


#LOOP
if __name__ == "__main__":
    app = AIR()
    app.mainloop()
