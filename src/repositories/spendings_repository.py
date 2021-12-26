"""Spendings repository"""
from database_connection import get_database_connection

class SpendingsRepository:
    """Class for handling spendings"""
    def __init__(self, connection):
        self.connection = connection

    def set_sums(self, username, spending):
        """Sets category sums to zero"""
        cursor = self.connection.cursor()
        cursor.execute('insert into categories (username, Groceries, Clothes, Technology, Other) \
                        values (?,?,?,?,?)',
                        (username,spending.summa,spending.summa,spending.summa,spending.summa,))
        self.connection.commit()

    def increase_sum(self, username, summa, category):
        """Increases sum by inserted value"""
        if isinstance(summa, int) or isinstance(summa, float):
            cursor = self.connection.cursor()
            nro = self.return_sum(username, category)
            cursor.execute('UPDATE categories SET (%s) = ? WHERE username =?' \
                            % (category),((nro+summa),username,))
            self.connection.commit()
        else:
            return

    def return_sum(self, username, category):
        '''Returns sum for a specified category
        Args:
            username: current user's username
            category: spendings category
        Returns:
            sum for specified category'''
        cursor = self.connection.cursor()
        cursor.execute('SELECT (%s) FROM categories WHERE username =?' \
                        %(category),(username,))
        gsum = cursor.fetchone()
        return float(gsum[0])

    def get_columnlist(self):
        '''Returns a list of columns in categories table
        Returns:
            list of columns in categories table'''
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
