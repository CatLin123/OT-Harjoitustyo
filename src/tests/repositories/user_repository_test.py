"""Testing user functions"""
import unittest
from repositories.user_repository import user_repository
from repositories.spendings_repository import spendings_repository
from entities.user import User
from database_connection import get_database_connection, initialize_database
from services.budget_service import budget_service



class TestUserRepository(unittest.TestCase):
    """Test class"""
    def setUp(self):
        spendings_repository.delete_all()
        user_repository.delete_all()
        self.user_troll = User("troll", "trollpassword", 100.0, 0.0)
        budget_service.create_user(self.user_troll.username, self.user_troll.password, self.user_troll.budget)

    def test_create_username(self):
        """Tests user creation"""
        self.assertEqual(self.user_troll.username, "troll")
    
    def test_create_password(self):
        """Tests password creation"""
        self.assertEqual(self.user_troll.password, "trollpassword")

