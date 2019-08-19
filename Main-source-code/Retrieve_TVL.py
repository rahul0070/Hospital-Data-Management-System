from tkinter import *
from tkinter.ttk import *
import sqlite3
import os
import re

def open_file(i):
    lio = li.get(ACTIVE)
    lion = lio.split('      ')
    y = lion[0] + '.txt'
    pr= os.getcwd()
    os.chdir('Case_files_TVL')
    os.popen(y)
    os.chdir(pr)


def disp_ph():
    li.config(width=30)
    ph = e1.get()
    i = 0
    ph = (ph + '*')
    cur = conn.execute('select * from Record_TVL')
    for row in cur:
        result = re.match(ph, row[6], re.IGNORECASE)
        if result:
            li.insert(i, str(row[2]) + '      ' + str(row[0]) + '      ' + row[6])
        i = i + 1
    cur.close()
    li.bind('<Double-1>', open_file)
    li.pack()


def disp_occ():
    li.config(width=30)
    occ = e1.get()
    i = 0
    occ = (occ + '*')
    cur = conn.execute('select * from Record_TVL')
    for row in cur:
        result = re.match(occ, row[7], re.IGNORECASE)
        if result:
            li.insert(i, str(row[2]) + '      ' + str(row[0]) + '      ' + row[7])
        i = i + 1
    cur.close()
    li.bind('<Double-1>', open_file)
    li.pack()


def disp_diag():
    li.config(width=30)
    dia = e1.get()
    i = 0
    diag = (dia + '*')
    cur = conn.execute('select * from Record_TVL')
    for row in cur:
        result = re.match(diag, row[5], re.IGNORECASE)
        if result:
            li.insert(i, str(row[2]) + '      ' + str(row[0]) + '      ' + row[5])
        i = i + 1
    cur.close()
    li.bind('<Double-1>', open_file)
    li.pack()


def disp_by_date():
    li.config(width=30)
    dx = str(e1.get())
    i = 0
    cur = conn.execute("select * from Record_TVL")
    for row in cur:
        if row[3] == dxs:
            li.insert(i, str(row[2]) + '      ' + str(row[0]))
        i = i + 1
    cur.close()
    li.pack()


def disp_name():
    nm = e1.get()
    li.config(width=30)
    conn = sqlite3.connect('Record_database.db')
    i = 0
    nm = (nm + '*')
    cur = conn.execute('select * from Record_TVL')
    for row in cur:
        result = re.match(nm, row[0], re.IGNORECASE)
        if result:
            li.insert(i, str(row[2]) + '      ' + str(row[0]))
        i = i + 1

    cur.close()
    li.bind('<Double-1>', open_file)
    li.pack()


def search():
    li.delete(0, END)
    x = e1.get()
    y = var.get()
    if y == 'Reg no':
        y = x + '.txt'
        os.chdir(r'Case_files_TVL')
        os.popen(y)
    elif y == 'Date':
        disp_by_date()
    elif y == 'Name':
        disp_name()
    elif y == 'Diagnosis':
        disp_diag()
    elif y == 'Phone':
        disp_ph()
    elif y == 'Occupation':
        disp_occ()  
    else:
        l4.config(text='ENTER A VALID CATEGORY')       


fr = Tk()
fr.title('Retrieve')
fr.config(height=500, width=100)

conn = sqlite3.connect("Record_database.db")
l0 = Label(fr, text='  ')
l1 = Label(fr, text="          GOMATHI HOMOEO CLINIC          ")
l2 = Label(fr, text="SEARCH BY:")
e1 = Entry(fr)
e1.focus()
o = ['-SELECT-','Name', 'Reg no', 'Date', 'Diagnosis', 'Phone', 'Occupation']
var = StringVar(fr)
var.set(o[0])
o1 = OptionMenu(fr, var, *o)
b1 = Button(fr, text="SUBMIT", command=search)
fr.bind('<Return>', search)
l3 = Label(fr, text='   ')
li = Listbox(fr)
lx = Listbox(fr)
l4 = Label(fr)
l1.pack()
l0.pack()
l2.pack()
o1.pack()
e1.pack()
b1.pack()
l4.pack()
l3.pack()

fr.mainloop()
