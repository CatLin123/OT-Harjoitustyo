import unittest
from entities.spendings import Category, Category_list


class TestSpendings(unittest.TestCase):
    def setUp(self):
        self.test_spendings = Category("Groceries")

    def test_adding_summa(self):
        self.test_spendings.add_summa(2)
        self.assertEqual("moi","moi")