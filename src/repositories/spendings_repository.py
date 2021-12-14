
from entities.user import User
from entities.spendings import Category
from database_connection import get_database_connection


class SpendingsRepository:

    def __init__(self, connection):
        self.connection = connection

    def find_all(self):
        """Returns all category sums"""
        cursor = self.connection.cursor()
        cursor.execute('select * from categories')
        rows = cursor.fetchall()
        #return list(map(get_category_by_row,rows))

    def find_by_username(self, username):
        """Returns user based on username"""
        cursor = self.connection.cursor()
        cursor.execute('select * from categories where username =?',(username,))
        
        row = cursor.fetchone()

        #return get_category_by_row(row)

    def set_sums(self, username, spending):
        """Sets category sums to zero"""
        cursor = self.connection.cursor()
        cursor.execute('insert into categories (username, Groceries, Clothes, Technology, Other) values (?,?,?,?,?)',(username,spending.summa,spending.summa,spending.summa,spending.summa,))
        self.connection.commit()

    def increase_sum(self, username, summa, category):
        """Increases sum by inserted value"""
        cursor = self.connection.cursor()
        nro = self.return_sum(username, category)
        cursor.execute('UPDATE categories SET (%s) = ? WHERE username =?'% (category),((nro+summa),username,))  
        self.connection.commit()

    def return_sum(self, username, category):
        cursor = self.connection.cursor()
        cursor.execute('SELECT (%s) FROM categories WHERE username =?'%(category),(username,))
        gsum = cursor.fetchone()
        return float(gsum[0])

    def get_columnlist(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from categories')
        names = list(map(lambda x: x[0], cursor.description))
        return names

    def delete_all(self):
        """Deletes all categories"""
        cursor = self.connection.cursor()
        cursor.execute('delete from categories')
        self.connection.commit()
 

spendings_repository = SpendingsRepository(get_database_connection())