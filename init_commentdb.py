import sqlite3

connection = sqlite3.connect('comments.db')


with open('comments.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()