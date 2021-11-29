'''Tests'''
import unittest
from entities.spendings import Category, CategoryList

class TestCategory(unittest.TestCase):
    '''Test category class'''
    def setUp(self):
        self.test_spendings = Category("Groceries")

    def test_adding_summa(self):
        '''Test adding summa'''
        self.test_spendings.add_summa(2)
        self.assertEqual(self.test_spendings.getsumma(),2)

class TestCategoryList(unittest.TestCase):
    '''Test category list class'''
    def setUp(self):
        self.test_spendings = CategoryList(["Groceries", "Technologies", "Restaurants"])

    def test_get_name(self):
        name = self.test_spendings.get_name(2)
        self.assertEqual(name, "Restaurants")

    def test_get_sum(self):
        self.test_spendings.get_add_summa(2,4)
        summa = self.test_spendings.get_sum(2)
        self.assertEqual(summa,4)