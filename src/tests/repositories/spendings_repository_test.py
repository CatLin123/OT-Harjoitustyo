'''Tests'''
import unittest
from entities.spendings import Category
from repositories.spendings_repository import spendings_repository 
from repositories.user_repository import user_repository
from services.budget_service import budget_service

class TestCategory(unittest.TestCase):
    '''Test category class'''
    def setUp(self):
        """Setup function"""
        self.test_spending = Category()

    def test_sum_value(self):
        """Test sum values"""
        self.assertEqual(float(self.test_spending.summa), 0.0)

class TestSpendingsRepository(unittest.TestCase):
    '''Testing SpendingsRepository'''
    def setUp(self):
        spendings_repository.delete_all()
        user_repository.delete_all()
        self.testi_user = budget_service.create_user("testi", "testisalasana", 100.0)
        self.tokatesti_user = budget_service.create_user("tokatesti", "testisalasana", 100.0)

    def test_set_sums(self):
        """Test returning sums"""
        spending = Category()
        spendings_repository.set_sums("tokatesti",spending)
        summa = spendings_repository.return_sum("tokatesti", "Groceries")
        self.assertEqual(summa, 0.0)

    def test_return_sums_groceries(self):
        """Test returning sums for groceries"""
        summa = spendings_repository.return_sum("testi", "Groceries")
        self.assertEqual(summa, 0.0)

    def test_return_sums_technology(self):
        """Test returning sums for technology"""
        summa = spendings_repository.return_sum("testi", "Technology")
        self.assertEqual(summa, 0.0)

    def test_return_sums_clothes(self):
        """Test returning sums for clothes"""
        summa = spendings_repository.return_sum("testi", "Clothes")
        self.assertEqual(summa, 0.0)
    
    def test_return_sums_other(self):
        """Test returning sums for other"""
        summa = spendings_repository.return_sum("testi", "Other")
        self.assertEqual(summa, 0.0)

    def test_increase_sum_groceries(self):
        """Test increasing sums for groceries"""
        spendings_repository.increase_sum("tokatesti", 5, "Groceries")
        summa = spendings_repository.return_sum("tokatesti", "Groceries")
        self.assertEqual(summa, 5.0)

    def test_increase_sum_technology(self):
        """Test increasing sum for technology"""
        spendings_repository.increase_sum("tokatesti", 5, "Technology")
        summa = spendings_repository.return_sum("tokatesti", "Technology")
        self.assertEqual(summa, 5.0)

    def test_increase_sum_clothes(self):
        """Test increasing sum for clothes"""
        spendings_repository.increase_sum("tokatesti", 5.0, "Clothes")
        summa = spendings_repository.return_sum("tokatesti", "Clothes")
        self.assertEqual(summa, 5.0)

    def test_increase_sum_other(self):
        """Test increasing sum for other"""
        spendings_repository.increase_sum("tokatesti", 10, "Other")
        spendings_repository.increase_sum("tokatesti", 20, "Other")
        summa = spendings_repository.return_sum("tokatesti", "Other")
        self.assertEqual(summa, 30.0)

    def test_increase_sum_large_input(self):
        """Test increasing sum with large input"""
        spendings_repository.increase_sum("tokatesti", 10, "Other")
        spendings_repository.increase_sum("tokatesti", 100, "Other")
        summa = spendings_repository.return_sum("tokatesti", "Other")
        self.assertEqual(summa, 110.0)

    def test_increase_sum_decimal_other(self):
        """Test increasing sum with decimal"""
        spendings_repository.increase_sum("tokatesti", 10.1, "Other")
        spendings_repository.increase_sum("tokatesti", 100.1, "Other")
        summa = spendings_repository.return_sum("tokatesti", "Other")
        self.assertEqual(str(round(summa, 2)),str(110.20))

    def test_increase_sum_decimal_groceries(self):
        """Test increasing sum with decimal for groceries"""
        spendings_repository.increase_sum("tokatesti", 10.2, "Groceries")
        spendings_repository.increase_sum("tokatesti", 200.3, "Groceries")
        summa = spendings_repository.return_sum("tokatesti", "Groceries")
        self.assertEqual(str(round(summa, 2)),str(210.50))

    def test_increase_sum_decimal_clothes(self):
        """Test increasing sum with decimal for groceries"""
        spendings_repository.increase_sum("tokatesti", 10.2, "Clothes")
        spendings_repository.increase_sum("tokatesti", 300.3, "Clothes")
        summa = spendings_repository.return_sum("tokatesti", "Clothes")
        self.assertEqual(str(round(summa, 2)),str(310.50))

    def test_increase_sum_decimal_technology(self):
        """Test increasing sum with decimal for technology"""
        spendings_repository.increase_sum("tokatesti", 10.3, "Technology")
        spendings_repository.increase_sum("tokatesti", 500.4, "Technology")
        summa = spendings_repository.return_sum("tokatesti", "Technology")
        self.assertEqual(str(round(summa, 2)),str(510.70))

    def test_increase_sum_false_input(self):
        """Test increasing sum with string"""
        spendings_repository.increase_sum("tokatesti", "ss", "Technology")
        summa = spendings_repository.return_sum("tokatesti", "Technology")
        self.assertEqual(summa,0.0)

    def test_get_column_list(self):
        """Test returning columns for categories table"""
        cols = spendings_repository.get_columnlist()
        self.assertEqual(cols, ['username', 'Groceries', 'Clothes', 'Technology', 'Other'])

