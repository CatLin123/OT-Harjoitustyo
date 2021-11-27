import sqlite3
from tkinter import *
#from PIL import ImageTk, Image


def get_database_connection():
    conn = sqlite3.connect('budget_app.db')
    return conn

def drop_tables(get_database_connection):
    cursor = get_database_connection().cursor()

    cursor.execute("""
    drop table if exits users;
    """)

    get_database_connection().commit()

def create_tables(connection):
    #Create a database or connect to one

    #Create cursor
    cursor = get_database_connection().cursor()

    #create table

    cursor.execute("""create table users (
        user_name text,
        password text,
    );
    """)
    get_database_connection().commit()


def initialize_database():
    """Initializes database table
    """

    conn = get_database_connection()

    drop_tables(conn)
    create_tables(conn)


if __name__ == '__main__':
    initialize_database()

