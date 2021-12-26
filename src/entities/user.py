"""User class"""
class User:
    """Class defining a specific user
    Attributes:
        username: string
        password: string
    """
    def __init__(self, username, password, budget, spent):
        """Function for creating new user
        """

        self.username = username
        self.password = password
        self.budget = budget
        self.spent = spent
