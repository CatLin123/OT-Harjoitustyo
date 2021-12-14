"""Testing user functions"""
import unittest
from repositories.user_repository import user_repository
from repositories.spendings_repository import spendings_repository
from entities.user import User
from database_connection import get_database_connection, initialize_database
from services.budget_service import budget_service

class TestBudgetService(unittest.TestCase):
    def setUp(self):
        self.budget_service = budget_service
        spendings_repository.delete_all()
        user_repository.delete_all()
        budget_service.create_user("testi", "testisalasana", 100.0)

    def test_category_sum_is_set(self):
        summa = budget_service.get_sum("Technology")
        self.assertEqual(float(summa), 0.0)


    