from tkinter import *
from tkinter.ttk import *

def fg():
    password = e1.get()
    if password == 'kalaibina3781':
        import Reboot_database
        t1.config(text='DATABASE REBOOTED SUCCESSFULLY')
    else:
        t1.config(text='WRONG PASSWORD')

fr = Tk()
fr.geometry("%dx%d%+d%+d" % (270, 260, 250, 125))
l1 = Label(fr, text='ADMINISTRATION', font=('Helvetica', 12))
l2 = Label(fr, text='WELCOME RAHUL')
l3 = Label(fr, text='Enter password to continue:')
e1 = Entry(fr)
b1 = Button(fr, text='SUBMIT', command=fg)
e1.focus()
t1 = Label(fr)
j = Label(fr)
k = Label(fr)
u = Label(fr)

k.pack()
l1.pack()
j.pack()
l2.pack()
l3.pack()
e1.pack()
b1.pack()
u.pack()
t1.pack()
fr.mainloop()