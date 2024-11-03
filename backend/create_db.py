import sqlite3

def create_database(filename):
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
    )
    ''')

    connection.commit()
    connection.close()