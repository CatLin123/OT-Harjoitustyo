from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row[0], row[1]) if row else None

class UserRepository:
    """Class for user related database functions"""
    def __init__(self,connection):
        """Connection: = Database connection conn object"""
        self.connection = connection

    def find_all(self):
        """Returns all users"""
        cursor = self.connection.cursor()
        cursor.execute('select * from users')
        rows = cursor.fetchall()
        return list(map(get_user_by_row,rows))

    def find_by_username(self, username):
        """Returns user based on username"""
        cursor = self.connection.cursor()
        cursor.execute('select * from users where username =?',(username,))
        
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Creates new user"""
        cursor = self.connection.cursor()
        cursor.execute('insert into users (username, password) values (?,?)', (user.username, user.password))
        self.connection.commit()
        
        return user

    def delete_all(self):
        """Deletes all users"""
        cursor = self.connection.cursor()
        cursor.execute('delete from users')
        self.connection.commit()

user_repository = UserRepository(get_database_connection())
