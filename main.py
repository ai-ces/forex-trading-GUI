
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np


# // main window

window = tk.Tk()
window.geometry("1080x640")
window.wm_title("Trading")

# // pwindow
pw = ttk.PanedWindow(window, orient= tk.HORIZONTAL)
pw.pack(fill = tk.BOTH, expand= True)


w2 = ttk.PanedWindow(pw, orient= tk.VERTICAL)

# frames

frame1 = ttk.Frame(pw, width= 360, height= 640, relief= tk.SUNKEN)
frame2 = ttk.Frame(pw, width= 720, height= 400, relief= tk.SUNKEN)
frame3 = ttk.Frame(pw, width= 720, height= 240, relief= tk.SUNKEN)

w2.add(frame2)
w2.add(frame3)

pw.add(w2)
pw.add(frame1)

# frame1 : treeview, open trade button

item = ""

def callback(event):
    global item
    item = treeview.identify("item", event.x,event.y)
    print("Clicked: ", item)

treeview = ttk.Treeview(frame1)
treeview.grid(row = 0, column= 1, padx= 25, pady= 25)
treeview.insert("", "0", "Major", text= "Major")
treeview.insert("Major", "1", "EUR/USD", text= "EUR/USD")
treeview.insert("", "2", "Minor", text= "Minor")
treeview.insert("Minor", "3", "EUR/GBR", text= "EUR/GBR")
treeview.bind("<Double-1>",callback)

def openTrade():
    print("OpenTrade")


open_button = tk.Button(frame1, text= "Open Trading", command = openTrade)
open_button.grid(row = 2, column= 1, padx= 5, pady= 5)

#frame2: tab view, radio button, button, result(Labelframe), plot

tabs = ttk.Notebook(frame2, width= 540, height= 300)
tabs.place(x = 25, y = 25)

tab1 = ttk.Frame(tabs, width= 50, height= 50)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text= "Line")
tabs.add(tab2, text= "Scatter", compound= tk.LEFT)

method = tk.StringVar()
tk.Radiobutton(frame2, text= "m1:", value= "m1", variable= method).place(x = 580, y= 100)
tk.Radiobutton(frame2, text= "m2:", value= "m2", variable= method).place(x = 580, y= 125)

label_frame = tk.LabelFrame(frame2, text= "Result", width= 100, height= 150)
label_frame.place(x = 580, y = 25)

tk.Label(label_frame,text= "Buy: ", bd = 3).grid(row= 0, column= 0)
tk.Label(label_frame, text= "Sell: ", bd = 3).grid(row= 1, column= 0)

def startTrading():
    print("startTrading")

start_button = tk.Button(frame2, text= "Start Trading", command= startTrading)
start_button.place(x= 580, y= 150)
start_button.config(state= "disabled")

#frame3: text editor (fundamental analysis), scroll bar

textBox = tk.Text(frame3, width= 70, height= 10, wrap= "word")
textBox.grid(row= 0, column= 0, padx= 25, pady= 25)
scroll = tk.Scrollbar(frame3, orient= tk.VERTICAL, command= textBox.yview)
scroll.grid(row = 0, column= 1, sticky= tk.N + tk.S, pady = 10)
textBox.config(yscrollcommand= scroll.set)

window.mainloop()