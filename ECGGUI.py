import tkinter as tk
import numpy as np
import csv
from matplotlib import pyplot as plt
from matplotlib import style
from tkinter import *


LARGE_FONT = ("Verdana", 12)

class ecgapp(tk.Tk):

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="snew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#functions for buttons
def plotecg(param):
    style.use('ggplot')
    t,v=np.loadtxt('C:/Users/Administrator/Desktop/mfiles/JohnECG.txt',unpack=True)

    #t,v=csv.reader(open('C:/Users/Administrator/Desktop/mfiles/JohnECG.csv','rb'),delimiter=',')
    plt.plot(t,v)
    plt.title('ECG')
    plt.ylabel('voltage')
    plt.xlabel('time')
    plt.show()

#def uploaddata():
    

class StartPage(tk.Frame): #makes a new page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Place ECG data in txt format in the directory", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #add button to execute function plotecg
        button1 = tk.Button(self, text="Plot the ECG",
                            command=lambda: plotecg("this worked"))
        button1.pack()



app = ecgapp()
app.mainloop()








