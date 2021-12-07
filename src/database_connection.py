import sqlite3
from tkinter import *
#from PIL import ImageTk, Image


def get_database_connection():
    conn = sqlite3.connect('budget_app')
    return conn

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
    drop table if exists users;
    ''')

    connection.commit()

def create_tables(connection):
 
    cursor = connection.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users 
                    (username text primary key, password text)
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

