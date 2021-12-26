"""Testing user functions"""
import unittest
from repositories.user_repository import user_repository
from repositories.spendings_repository import spendings_repository
from entities.user import User
from services.budget_service import budget_service

class TestUserRepository(unittest.TestCase):
    """Test class"""
    def setUp(self):
        """Setup function"""
        spendings_repository.delete_all()
        user_repository.delete_all()
        self.user_troll = User("troll", "trollpassword", 100.0, 0.0)
        self.user_dude = User("dude", "dudepassword", 200.0, 0.0)
        budget_service.create_user(self.user_troll.username,
                                    self.user_troll.password,
                                    self.user_troll.budget)
        budget_service.create_user(self.user_dude.username,
                                    self.user_dude.password,
                                    self.user_dude.budget)
        
    def test_create_username(self):
        """Tests user creation"""
        self.assertEqual(self.user_troll.username, "troll")
    
    def test_create_password(self):
        """Tests password creation"""
        self.assertEqual(self.user_troll.password, "trollpassword")

    def test_find_all(self):
        """Test finding all users"""
        users = user_repository.find_all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_troll.username)
        self.assertEqual(users[1].username, self.user_dude.username)

    def test_find_by_username(self):
        """Test finding user by username"""
        user = user_repository.find_by_username(self.user_troll.username)
        self.assertEqual(user.username, self.user_troll.username)

    def test_adjust_monthly_budget(self):
        """Test adjusting monthly budjet"""
        user_repository.adjust_monthly_budget(self.user_troll, 10, "Spent")
        spent = user_repository.get_budget(self.user_troll,"Spent")
        self.assertEqual(spent, 10.0)

    def test_get_column_list(self):
        """Test returning columns for users table"""
        cols = user_repository.get_columnlist()
        self.assertEqual(cols, ['username', 'password', 'Left', 'Spent'])
