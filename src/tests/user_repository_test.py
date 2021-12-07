"""Testing user functions"""
import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    """Test class"""
    def setUp(self):
        self.user_troll = User("troll", "trollpassword")

    def test_create_username(self):
        user_repository.delete_all()
        user_repository.create(self.user_troll)
        all_users = user_repository.find_all()
        self.assertEqual(all_users[0].username, self.user_troll.username)
    
    def test_create_password(self):
        user_repository.delete_all()
        user_repository.create(self.user_troll)
        all_users = user_repository.find_all()
        self.assertEqual(all_users[0].password, self.user_troll.password)