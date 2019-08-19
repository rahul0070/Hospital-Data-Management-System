from tkinter import *
from tkinter.ttk import *
import sqlite3
import os


def fileg(reg):
    file_name = 'Case_files_KVP/' + str(reg) + ".txt"
    lines = []
    with open(file_name) as filex:
        for line1 in filex:
            lines.append(line1)
        filex.close()
    l = len(lines)
    info_str = ''
    for i in range(l):
        if(i>10):
            info_str = info_str+lines[i]
            print(lines[i])
    
    return info_str


def file_writer(name, age, d, sex, diagnosis, ph, occ):
    info = t1.get(1.0, END)
    rec = ex.get()
    l = [name, str(age), sex, str(rec), d, diagnosis, ph, occ, info]
    l2 = ['Name:      ', 'Age:         ', 'Sex:         ', 'Reg no:    ', 'Date:       ', 'Diagnosis: ', 'Phone:   ','Occupation: ', '-']

    file_name = 'Case_files_KVP/' + str(rec) + ".txt"
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
    l13.config(text='DATABASE UPDATED')



def retrieve():
    ch = ex.get()
    info_str = fileg(ch)
    flag = 0
    conn = sqlite3.connect('Record_database.db')
    cur = conn.execute('select * from Record_KVP')
    for row in cur:
        if ch == row[2]:
            e1.insert(0, row[0])
            e2.insert(0, row[1])
            e4.insert(0, row[4])
            e3.insert(0, row[2])
            e5.insert(0, row[3])
            e6.insert(0, row[5])
            e7.insert(0, row[6])
            e8.insert(0, row[7])
            t1.insert(1.0, info_str)
            e1.focus()
            flag = 1
            b1.grid(row=15, column=1, columnspan=2)
    if flag == 0:
        l13.config(text='FILE NOT FOUND')


def update():
    reg = ex.get()
    conn = sqlite3.connect('Record_database.db')
    conn.execute('update Record_KVP SET name=?, age=?, doe=?, sex=?, diag=?, phone=?, occupation=? where file_no=?', (e1.get(), e2.get(), e5.get(), e4.get(), e6.get(), e7.get(), e8.get(), reg))
    conn.commit()
    conn.close()
    file_name = 'Case_files_KVP/' + reg + ".txt"
    try:
        os.remove(file_name)
    except:
        l13.config(text='FILE NOT FOUND')    
    file_writer(e1.get(), e2.get(), e5.get(), e4.get(), e6.get(), e7.get(), e8.get())



fr = Tk()
lx = Label(fr, text='UPDATE DATABASE')
ly = Label(fr, text='   ')
lz = Label(fr, text="Enter file's reg.no to updated:")
ex = Entry(fr)
ex.focus()
bx = Button(fr, text='SUBMIT', command=retrieve)

lx.grid(row=0,column=1,columnspan=2)
ly.grid(row=1,column=1,columnspan=2)
lz.grid(row=2,column=1)
ex.grid(row=2,column=2)
bx.grid(row=3,column=1,columnspan=2)

#UPDATE SECTION

o = ['-SELECT-','Male', 'Female']
var = StringVar(fr)
var.set(o[0])

o1 = OptionMenu(fr, var, *o)
l2 = Label(fr, text="Name:")
e1 = Entry(fr)
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
b1 = Button(fr, text="UPDATE", command=update)
t1 = Text(fr)
t1.config(width=50, height=10)
l13 = Label(fr)

l2.grid(row=4, column=1)
l3.grid(row=5, column=1)
#l4.grid(row=7, column=1)
l6.grid(row=6, column=1)
l7.grid(row=8, column=1)
l8.grid(row=9, column=1)
l11.grid(row=10, column=1)
l12.grid(row=11, column=1)

e1.grid(row=4, column=2)
e2.grid(row=5, column=2)
#e3.grid(row=7, column=2)
o1.grid(row=6, column=2)
e5.grid(row=8, column=2)
e6.grid(row=9, column=2)
e7.grid(row=10, column=2)
e8.grid(row=11, column=2)
t1.grid(row=14, column=1, columnspan=2)
l13.grid(row=16, column=1, columnspan=2)

fr.mainloop()

