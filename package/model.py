import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """This is an function use to fonmat the json when retirve from the  mysql database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

conn.execute('''CREATE TABLE if not exists doctor
(doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
doc_name TEXT NOT NULL,
doc_qual TEXT NOT NULL,
doc_spec TEXT NOT NULL,
doc_ph_no TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists patient
(pat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_name TEXT NOT NULL,
pat_disease TEXT NOT NULL,
pat_date DATE NOT NULL,
pat_address TEXT NOT NULL,
pat_ph_no TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists other
(oth_id INTEGER PRIMARY KEY AUTOINCREMENT,
oth_name TEXT NOT NULL,
oth_role TEXT NOT NULL,
oth_ph_no TEXT NOT NULL);''')


conn.execute('''CREATE TABLE if not exists medicine
(med_id INTEGER PRIMARY KEY AUTOINCREMENT,
med_name TEXT NOT NULL,
med_power TEXT NOT NULL,
med_brand TEXT NOT NULL,
med_mfg TEXT NOT NULL,
med_exp TEXT NOT NULL,
med_quan TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists user
(id	INTEGER NOT NULL,
uname TEXT NOT NULL,
email TEXT NOT NULL,
pswd TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists covidpatient
(phypat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_name TEXT NOT NULL,
pat_date DATE NOT NULL,
pat_address TEXT NOT NULL,
pat_ph_no TEXT NOT NULL,
pat_amount TEXT NOT NULL);''')
