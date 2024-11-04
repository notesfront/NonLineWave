import os
from backend import *
import sqlite3
# create_db.create_test_db()

if not os.path.isdir('participant.db'):
        create_database('participant.db')

a = [Person(fname='Саша', lname='Волкова', email='test@test.ru'), Person(fname='Андрей',  lname='Волкова', email='test@test.ru')]

conn = sqlite3.connect('participant.db')

for p in a:
    p.add_in_db(conn)
    # print(p.id)