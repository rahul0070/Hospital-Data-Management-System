import sqlite3
from tkinter import *
from tkinter.ttk import*


fr = Tk()
la1 = Label(fr, text='NAME')
la2 = Label(fr, text='FILE_NO')
la3 = Label(fr, text='DATE')
l1 = Listbox(fr, width=15)
l2 = Listbox(fr, width=15)
l3 = Listbox(fr, width=15)
i = 1
conn = sqlite3.connect("Record_database.db")
cur = conn.execute("select * from Record_TVL order by file_no")
for row in cur:
    i = i+1
    l1.insert(i, row[0])
    l2.insert(i, row[2])
    l3.insert(i, row[3])

la1.grid(row=0,column=1)
la2.grid(row=0,column=2)
la3.grid(row=0,column=3)
l1.grid(row=1,column=1)
l2.grid(row=1,column=2)
l3.grid(row=1,column=3)
fr.mainloop()