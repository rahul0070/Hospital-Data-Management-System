import os
import sys
from tkinter import *
from tkinter.ttk import *

def dg():
	import Main_TVL

def df():
	import Retrieve_TVL

def gg():
    import Admin	

def hn():
	import Display_record_TVL

def kl():
    import Update_KVP	

fr = Tk()
fr.geometry("%dx%d%+d%+d" % (300, 260, 250, 125))
fr.title('GOMATHI HOMOEO CLINIC')
l0 = Label(fr, text='GOMATHI HOMOEO CLINIC')
l1 = Label(fr, text='      TIRUNELVELI PATIENTS RECORD       ')
l2 = Label(fr, text='  ')
b1 = Button(fr, text='Enter record', command=dg, width=15)
b2 = Button(fr, text='Retrieve record', command=df, width=15)
bu = Button(fr, text='Update record', command=kl, width=15)
bx = Button(fr, text='Admin', command=gg, width =15)
bf = Button(fr, text='Display record', command=hn, width=15)
b4 = Button(fr, text='Exit', command=lambda: sys.exit(), width=15)
lo = Label(fr,text='  ')
lx = Label(fr, text='Version 1.1.1')

l0.pack()
l1.pack()
l2.pack()
b1.pack()
b2.pack()
bf.pack()
bu.pack()
bx.pack()
b4.pack()
lo.pack()
lx.pack()
fr.mainloop()