class User:
    """Class defining a specific user
    Attributes:
        username: string 
        password: string 
    """

    def __init__(self, username, password):
        """Function for creating new user
        """

        self.username = username
        self.password = password