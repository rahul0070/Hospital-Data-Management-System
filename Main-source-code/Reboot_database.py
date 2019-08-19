import sqlite3
import os
import shutil

conn=sqlite3.connect("Record_database.db")

def re():
    print('Creating database...')
    try:
        conn.execute("create table Record_TVL (name varchar(20) default '-', age varchar(10) default '-', file_no varchar(20) not null, doe varchar(20) default '-', sex varchar(10), diag varchar(30) default '-', phone varchar(20) default '-', occupation varchar(20) default'-')")
        conn.commit()
    except:
        print('Database exists')
        conn.execute('delete from Record_TVL')
    conn.commit()

    try:
        conn.execute("create table Record_KVP (name varchar(20) default '-', age varchar(10) default '-', file_no varchar(20) not null, doe varchar(20) default '-', sex varchar(10), diag varchar(30) default '-', phone varchar(20) default '-', occupation varchar(20) default'-')")
        conn.commit()
    except:
        conn.execute('delete from Record_KVP')
        print('Database exists')
    conn.commit()
    conn.close()
    print('Database created')

def md():
    print('Creating Directories...')
    if not os.path.exists('Case_files_KVP'):
        os.mkdir('Case_files_KVP')
    if not os.path.exists('Case_files_TVL'):
        os.mkdir('Case_files_TVL')    


def rd():
    print('Removing directory...')
    try:
        shutil.rmtree('Case_files_KVP')
        shutil.rmtree('Case_files_TVL')
    except:
        print("Directoies doesn't exist...")
    md()


rd()
re()
