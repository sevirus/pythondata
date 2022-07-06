import sqlite3

def create_table():
    conn = sqlite3.connect('/Users/seonggyunjung/PYTHONDATA/pythondata/python_basic/03_db/business_card.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists business_card(
        idNumber integer,
        name text,
        callNumber integer,
        faxNumber integer,
        comName text
    )
    ''')


def bc_insert():

def bc_update():

def bc_delete():

def bc_list():