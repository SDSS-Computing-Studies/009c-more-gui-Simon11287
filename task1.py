

import tkinter as tk 
from tkinter import *
from tkinter import ttk
import math 

def triangle():
    a=a1.get()
    h=a2.get()
    b=a4.get()
    c=a3.get()
    if h=="" and a!= "" and b!= "" and c!= "":
        a=int(a)
        b=int(b)
        c=int(c)
        s=(a+b+c)/2
        A=math.sqrt(s*(s-a)*(s-b)*(s-c))
        A=("The Area is "+str(abs(A)))
    elif h!="" and b!="":
        b=int(b)
        h=int(h)
        A=(b*h/2)
        A=("The Area is "+str(abs(A)))
    else: 
        A=("The area cannot be calculated\n from the given information")
    eoutput.set(A)
win=tk.Tk()
win.title=("Triangle Calculator")
eoutput=StringVar()
answer=StringVar()
triangle1=PhotoImage(file="triangle.png")
l1=tk.Label(win,image=triangle1)
a1=Entry(win,width=6)
a2=Entry(win,width=6)
a3=Entry(win,width=6)
a4=Entry(win,width=6)
l4=Label(win,text="Enter in as much information about the\n triangle shown and I will calculate the area")
b1=Button(win,text="Calculate",command=triangle)
f1=Label(win,textvariable=eoutput)
win.geometry("500x400")
l1.pack()
a1.place(x=155,y=105)
a2.place(x=305,y=140)
a3.place(x=405,y=150)
a4.place(x=275,y=240)
l4.place(x=0,y=270)
b1.place(x=250,y=270)
f1.place(x=0,y=290)
win.mainloop()
