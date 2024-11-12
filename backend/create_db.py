import sqlite3
import os

def create_database(filename):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    userfname TEXT NOT NULL,
    usermname TEXT,
    userlname TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    docname INTEGER,
    status TEXT,
    sum INTEGER
    )
    ''')

    connection.commit()
    connection.close()

def create_test_db():
    if not os.path.isdir('./participant.db'):
        create_database('./participant.db')
    connection = sqlite3.connect('./participant.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Users (userfname, email, age) VALUES (?, ?, ?)''',
                    ('newuser', 'newuser@example.com', 28))

    connection.commit()
    connection.close()

# def add_person_into_db(data_person):
#     connection = sqlite3.connect('./participant.db')
#     cursor = connection.cursor()
#     for person in range(len(data_person)):
#         cursor.execute('''INSERT INTO Users (userfname, email, age) VALUES (?, ?, ?)''',
#                     ('newuser', 'newuser@example.com', 28))

#     connection.commit()
#     connection.close()