"""User repository"""
from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row[0], row[1], row[2], row[3]) if row else None

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
        """Creates new user   
        Args:
            user: user to be created"""
        cursor = self.connection.cursor()
        cursor.execute('insert into users (username, password, Left, Spent) values (?,?,?,?)',
                        (user.username, user.password, user.budget, 0.0))
        self.connection.commit()
        return user

    def get_budget(self,user,keyword):
        """Returns budget
        Args:
            user: current user
            keyword: specifies spent or left    
        Returns:
            Float from the database (spent or left)"""
        cursor= self.connection.cursor()
        cursor.execute('select (%s) from users where username=?'% \
                        (keyword),(user.username,))
        budget = cursor.fetchone()
        return float(budget[0])

    def adjust_monthly_budget(self,user,summa, keyword):
        """Adjusts budget
        Args:
            user: current user
            summa: sum that will be added to the monthly budget
            keyword: specifies spent or left"""
        cursor= self.connection.cursor()
        if keyword == "Left":
            cursor.execute('UPDATE users SET (%s) = ? WHERE username =?' \
                            % (keyword),((self.get_budget(user, keyword)-summa),user.username,))
        if keyword == "Spent":
            cursor.execute('UPDATE users SET (%s) = ? WHERE username =?' \
                            % (keyword),((self.get_budget(user, keyword)+summa),user.username,))
        self.connection.commit()
    
    def delete_all(self):
        """Deletes all users"""
        cursor = self.connection.cursor()
        cursor.execute('delete from users')
        self.connection.commit()

    def get_columnlist(self):
        '''Returns:
            All columns in the users table'''
        cursor = self.connection.cursor()
        cursor.execute('select * from users')
        names = list(map(lambda x: x[0], cursor.description))
        return names

user_repository = UserRepository(get_database_connection())
