"""Testing user functions"""
import unittest
from repositories.user_repository import user_repository
from repositories.spendings_repository import spendings_repository
from entities.user import User
from database_connection import get_database_connection
from services.budget_service import budget_service, InvalidCredentialsError

class TestBudgetService(unittest.TestCase):
    """Testing budget service"""
    def setUp(self):
        '''Setup class'''
        self.budget_service = budget_service
        spendings_repository.delete_all()
        user_repository.delete_all()
        self.user_anna = User("anna", "annansalasana", 100.0, 0.0)
        budget_service.create_user(self.user_anna.username,
                                    self.user_anna.password,
                                    self.user_anna.budget)
    
    def test_user_exists(self):
        """Testing user exists"""
        self.assertEqual(self.user_anna.username, "anna")

    def test_login(self):
        """Testing login"""
        budget_service.login("anna","annansalasana")
        current_user = budget_service.get_current_user()
        self.assertEqual(current_user.username, "anna")
        self.assertEqual(current_user.password, "annansalasana")

    def test_monthly_budget(self):
        """Testing getting monthly budget"""
        budget_service.login("anna","annansalasana")
        budget = budget_service.get_monthly("left")
        self.assertEqual(budget, 100)

    def test_create_spending_left(self):
        """Testing creating spending and checking left"""
        budget_service.create_spending(10, "Technology")
        left = budget_service.get_monthly("left")
        self.assertEqual(left, 90)

    def test_create_spending_spent(self):
        """Testing creating spending and checking spent"""
        budget_service.create_spending(10, "Technology")
        spent = budget_service.get_monthly("spent")
        self.assertEqual(spent, 10)

    def test_get_sum_for_groceries(self):
        """Testing getting sum for groceries"""
        budget_service.create_spending(10, "Groceries")
        summa = budget_service.get_sum("Groceries")
        self.assertEqual(float(summa), 10.0)
        
    def test_get_sum_for_clothes(self):
        """Testing getting sum for clothes"""
        budget_service.create_spending(20, "Clothes")
        summa = budget_service.get_sum("Clothes")
        self.assertEqual(float(summa), 20.0)

    def test_get_sum_for_technology(self):
        """Testing getting sum for technology"""
        budget_service.create_spending(20, "Technology")
        summa = budget_service.get_sum("Technology")
        self.assertEqual(float(summa), 20.0)

    def test_get_sum_for_clothes(self):
        """Testing getting sum for clothes"""
        budget_service.create_spending(20, "Other")
        summa = budget_service.get_sum("Other")
        self.assertEqual(float(summa), 20.0)
        
    def test_category_sum_is_set(self):
        """Testing category sum is set"""
        '''Tests that category sum is 0.0'''
        summa = budget_service.get_sum("Technology")
        self.assertEqual(float(summa), 0.0)

    def test_get_columns_spendings(self):
        """Testing getting columns from categories table"""
        lista = budget_service.get_columns_spendings()
        self.assertEqual(lista, ["username", "Groceries", "Clothes", "Technology", "Other"])

    def test_get_columns_users(self):
        """Testing getting columns from users table"""
        lista = budget_service.get_columns_users()
        self.assertEqual(lista, ["username", "password", "Left", "Spent"])

    def test_logout(self):
        """Testing logging out"""
        budget_service.logout()
        user = budget_service.get_current_user()
        self.assertEqual(user, None)

    def test_login_with_invalid_username_and_password(self):
        """Testing logging in with invalid credentials"""
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.budget_service.login('testing', 'invalid')
        )

    def test_get_monthly_spent(self):
        """Testing getting monthly spent"""
        budget_service.login("anna", "annansalasana")
        spent = budget_service.get_monthly("Spent")
        self.assertEqual(spent, 0)

    def test_get_monthly_left(self):
        """Testing getting monthly left"""
        budget_service.login("anna", "annansalasana")
        spent = budget_service.get_monthly("Left")
        self.assertEqual(spent, 100)
