'''Create user view'''
import tkinter as tk
from services.budget_service import budget_service, UsernameExistsError

class CreateUserView:
    """Class for creating user"""
    def __init__(self, root, show_login_view):
        self.root = root
        self.frame = tk.Frame(master=self.root)
        self.user_name = None
        self.password = None
        self.show_login_view = show_login_view
        self.frame.place(relheight=0.8, relwidth=0.8)
        self.monthly_budget = None
        self.initialize()

    def pack(self):
        '''Pack'''
        self.frame.pack()

    def destroy(self):
        '''Destroy current view function'''
        self.frame.destroy()

    def show_error(self, message):
        '''Error message in case of invalid login details'''
        self.error_label = tk.Label(master=self.frame, text = message)
        self.error_label.pack()

    def user_handler(self):
        '''Show username field'''
        #create user
        username = self.username.get()
        password = self.password.get()
        budget = self.monthly_budget.get()

        if len(username) == 0 or len(password) == 0:
            self.show_error("Please submit username and password")
            return

        try:
            budget_service.create_user(username, password, budget)
            self.show_error("User created")
        except UsernameExistsError:
            self.show_error("Username already exists")

    def back_handler(self):
        '''Back to login'''
        self.show_login_view()

    def initialize_username(self):
        '''Show username field'''
        username_label = tk.Label(master=self.frame, text="Username")
        username_label.place(relx=0.1, rely=0.8, anchor =tk.W)
        username_label.pack()
        self.username =tk.Entry(master=self.frame)
        self.username.place(relx=0.9, rely=0.8, anchor = tk.E)
        self.username.pack()

    def initialize_password(self):
        '''Show password field'''
        password_label = tk.Label(master=self.frame, text="Password")
        password_label.pack()
        self.password = tk.Entry(master=self.frame)
        self.password.pack()

    def initialize_monthly_budget(self):
        """Set monthly budget"""
        budget_lable = tk.Label(master=self.frame, text="Monthly Budget")
        budget_lable.pack()
        self.monthly_budget = tk.Entry(master=self.frame)
        self.monthly_budget.pack()

    def initialize(self):
        '''Initialize'''
        info_label = tk.Label(master=self.frame, text="CREATE NEW USER")
        info_label.place(relx=0.1, rely=0.8, anchor =tk.W)
        info_label.pack()
        self.initialize_username()
        self.initialize_password()
        self.initialize_monthly_budget()
        back_button = tk.Button(master=self.frame, text="Create user", command=self.user_handler)
        back_button.place(relx=10, rely=1)
        back_button.pack()
        create_button = tk.Button(master=self.frame, text="Back to login", command=self.back_handler)
        create_button.place(relx=10, rely=1)
        create_button.pack()
