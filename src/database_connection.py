import sqlite3
from tkinter import *
#from PIL import ImageTk, Image


def get_database_connection():
    conn = sqlite3.connect('budget_app')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
    drop table if exists categories;
    ''')

    cursor.execute('''
    drop table if exists users;
    ''')

    connection.commit()

def create_tables(connection):
 
    cursor = connection.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users 
                    (username text primary key, password text, Left float, Spent float)
                ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS categories 
                    (username text, Groceries float, Clothes float, Technology float, Other float, FOREIGN KEY (username) REFERENCES users (username))
                ''')

    connection.commit()

def initialize_database():
    """Initializes database table
    """

    conn = get_database_connection()

    drop_tables(conn)
    create_tables(conn)


if __name__ == '__main__':
    initialize_database()

