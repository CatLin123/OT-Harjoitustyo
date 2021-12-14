'''Tests'''
import unittest
from entities.user import User
from entities.spendings import Category
from database_connection import get_database_connection, drop_tables, create_tables
from repositories.spendings_repository import spendings_repository 
from repositories.user_repository import user_repository
from services.budget_service import budget_service

class TestCategory(unittest.TestCase):
    '''Test category class'''
    def setUp(self):
        self.test_spending = Category()

    def test_sum_value(self):
        self.assertEqual(float(self.test_spending.summa), 0.0)

class TestSpendingsRepository(unittest.TestCase):
    '''Testing SpendingsRepository'''
    def setUp(self):
        spendings_repository.delete_all()
        user_repository.delete_all()
        budget_service.create_user("testi", "testisalasana", 100.0)
        budget_service.create_user("tokatesti", "testisalasana", 100.0)

    def test_return_sum(self):
        summa = spendings_repository.return_sum("testi", "Groceries")
        self.assertEqual(summa, 0.0)

    def test_increase_sum(self):
        spendings_repository.increase_sum("tokatesti", 5, "Groceries")
        summa = spendings_repository.return_sum("tokatesti", "Groceries")
        self.assertEqual(summa, 5.0)