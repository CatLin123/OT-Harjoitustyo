"""Service"""
from entities.spendings import Category
from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)
from repositories.spendings_repository import (spendings_repository as default_spendings_repository)

class InvalidCredentialsError(Exception):
    """Exception if credentials are invalid"""
    pass

class UsernameExistsError(Exception):
    """Exception if username exists"""
    pass

class BudgetService:
    """Application logic class"""

    def __init__(self,
                user_repository = default_user_repository,
                spendings_repository = default_spendings_repository):
        self.user = None
        self.user_repository = user_repository
        self.spendings_repository = spendings_repository

    def create_user(self, username, password, budget, login = True):
        """Creates new user and logs in
        Args:
            username: username
            password: password
            budget: chosen monthly budget
        Returns:
            Created user"""
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')
        user = self.user_repository.create(User(username,password,budget,0))
        spending = Category()
        self.spendings_repository.set_sums(username,spending)
        if login:
            self.user = user
        return user

    def logout(self):
        """Function for logging out user"""
        self.user = None

    def get_current_user(self):
        """Function for getting logged in user"""
        return self.user

    def login(self, username, password):
        """Function for logging in user"""
        user = self.user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self.user = user
        return user

    def get_monthly(self,keyword):
        '''Returns monthly budget for either spent or left
        Args:
            keyword: specifies spent or left
        Returns:
            Current spent or left budget'''
        user = self.user
        return self.user_repository.get_budget(user, keyword)

    def create_spending(self, sum_content, category_content):
        '''Creates spending'''
        user = self.user
        self.spendings_repository.increase_sum(user.username, sum_content, category_content)
        self.adjust_budget(sum_content, "Spent")
        self.adjust_budget(sum_content, "Left")

    def adjust_budget(self,sum_content, keyword):
        user = self.user
        self.user_repository.adjust_monthly_budget(user, sum_content, keyword)
    
    def get_sum(self, category):
        '''Gets sum for a category
        Args:
            category: category for a type of spending
        Returns:
            sum for the specified category'''
        user = self.user
        summa = self.spendings_repository.return_sum(user.username, category)
        return str(summa)

    def get_columns_spendings(self):
        '''Returns list of columns in categories table
        Returns:
            List of columns in categories table'''
        return self.spendings_repository.get_columnlist()

    def get_columns_users(self):
        '''Returns list of columns in users table
        Returns:
            List of columns in users table'''
        return self.user_repository.get_columnlist()
        
budget_service = BudgetService()
