from tkinter import *
from tkinter.ttk import *
import sqlite3
import datetime
import sys

def call(even):
    p1.step(amount=15)

def ch(even):
    check()    

def clr():
    print('Entering clr')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    t1.delete('1.0', END)
    l10.config(text="FILE ALREADY EXISTS")
    e1.focus()
    p1.stop()


def del_c():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    t1.delete('1.0', END)
    l10.config(text="DATA SUBMITED")
    e1.focus()
    p1.stop()


def check():
    rec = e3.get()
    flag = 0
    conn = sqlite3.connect("Record_database.db")
    cur = conn.execute("select file_no from Record_TVL")
    for i in cur:
        if (i[0] == rec):
            flag = 1
    if (flag == 1):
        print('File exists')
        clr()
    else:
        submit()


def file_writer(name, age, d, sex, diagnosis, ph, occ):
    info = t1.get(1.0, END)
    rec = e3.get()
    l = [name, str(age), sex, str(rec), d, diagnosis, ph, occ, info]
    l2 = ['Name:      ', 'Age:         ', 'Sex:         ', 'Reg no:    ', 'Date:       ', 'Diagnosis: ', 'Phone:   ','Occupation: ', '-']

    file_name = 'Case_files_TVL/' + str(rec) + ".txt"
    fob = open(file_name, "w+")

    fob.write("---------------CASE FILE: " + str(rec) + "--------------")
    fob.write('\n')
    for x in range(len(l)):
        fob.write(l2[x])
        if (x == 8):
            fob.write('--------------------DESCRIPTION--------------------')
            fob.write("\n")
        fob.write(l[x] + "\n")
    fob.close()
    del_c()


def submit():
    p1.start()
    conn = sqlite3.connect("Record_database.db")
    name = e1.get()
    age = e2.get()
    rec = e3.get()
    sex = var.get()
    if sex == '-Select-':
        sex = 'Not mentioned'
    ph = e7.get()
    occ = e8.get()
    # now = datetime.datetime.now()
    # d = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    d = e5.get()
    diagnosis = e6.get()
    conn.execute("insert into Record_TVL (name, age, file_no, doe, sex, diag, phone, occupation) values (?,?,?,?,?,?,?,?);",
                 (name, age, rec, d, sex, diagnosis, ph, occ))
    conn.commit()

    file_writer(name, age, d, sex, diagnosis, ph, occ)


fr = Tk()
fr.config(height=600, width=600)
fr.grid()

o = ['-Select-','Male', 'Female']
var = StringVar(fr)
var.set(o[0])

o1 = OptionMenu(fr, var, *o)
l1 = Label(fr, text="PATIENT RECORD TIRUNELVELI")
l2 = Label(fr, text="Name:")
e1 = Entry(fr)
e1.focus()
l3 = Label(fr, text="Age:")
e2 = Entry(fr)
l6 = Label(fr, text="Sex:")
e4 = Entry(fr)
l4 = Label(fr, text="Registration number:")
e3 = Entry(fr)
l7 = Label(fr, text="Date:")
e5 = Entry(fr)
l8 = Label(fr, text="Diagnosis:")
e6 = Entry(fr)
l11 = Label(fr, text='Phone no:')
e7 = Entry(fr)
l12 = Label(fr, text='Occupation')
e8 = Entry(fr)
t1 = Text(fr)
t1.config(width=50, height=10)
l5 = Label(fr, text="DESCRIPTION:")
l10 = Label(fr)
b1 = Button(fr, text="SUBMIT", command=check)
p1 = Progressbar(fr, orient='horizontal', length = 200, mode = 'determinate')


l1.grid(row=1, column=1, columnspan=2)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=5, column=1)
l6.grid(row=4, column=1)
l7.grid(row=6, column=1)
l8.grid(row=7, column=1)
l11.grid(row=8, column=1)
l12.grid(row=9, column=1)
l10.grid(row=13, column=1, columnspan=2)

e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=5, column=2)
o1.grid(row=4, column=2)
e5.grid(row=6, column=2)
e6.grid(row=7, column=2)
e7.grid(row=8, column=2)
e8.grid(row=9, column=2)

t1.grid(row=11, column=1, columnspan=2)
l5.grid(row=10, column=1, columnspan=2)
b1.grid(row=12, column=1, columnspan=2)
p1.grid(row=14, column=1, columnspan=2)

#fr.bind('<Return>',ch)
fr.bind('<Tab>',call)
fr.mainloop()
