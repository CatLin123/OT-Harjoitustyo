'''Login view'''
import tkinter as tk
from tkinter import ttk, StringVar, constants
from services.budget_service import budget_service, InvalidCredentialsError

class LoginView:
    '''Handles login attempts'''
    def __init__(self, root, getloggedin, create_user):
        self.root = root
        self.frame = tk.Frame(master=self.root)
        self.username_entry = None
        self.password_entry = None
        self.getloggedin = getloggedin
        self.create_user = create_user
        self.frame.place(relheight=0.8, relwidth=0.8)
        self.initialize()

    def pack(self):
        '''Pack function'''
        self.frame.pack()

    def destroy(self):
        '''Destroy current view function'''
        self.frame.destroy()

    def initialize_username_field(self):
        '''Show username field'''
        username_label = tk.Label(master=self.frame, text="Username")
        username_label.place(relx=0.1, rely=0.8, anchor =tk.W)
        username_label.pack()
        self.username_entry =tk.Entry(master=self.frame)
        self.username_entry.place(relx=0.9, rely=0.8, anchor = tk.E)
        self.username_entry.pack()
        self.error_variable = None
        self.error_label = None

    def initialize_password_field(self):
        '''Show password field'''
        password_label = tk.Label(master=self.frame, text="Password")
        password_label.pack()
        self.password_entry= tk.Entry(master=self.frame)
        self.password_entry.pack()

    def login_handler(self):
        '''Functioning for managing logins'''
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            budget_service.login(username,password)
            self.getloggedin()
        except InvalidCredentialsError:
            self.show_error("Invalid username or password")

    def user_handler(self):
        '''Button for creating new user'''
        self.create_user()
     
    def show_error(self, message):
        '''Error message in case of invalid login details'''
        self.error_label = tk.Label(master=self.frame, text = message)
        self.error_label.pack()

    def initialize(self):
        '''Login initializer'''
        self.initialize_username_field()
        self.initialize_password_field()
        login_button = tk.Button(master=self.frame, text="Log in", command=self.login_handler)
        login_button.place(relx=10, rely=1)
        login_button.pack()
        create_user_button = tk.Button(master=self.frame, text="Create user", command=self.user_handler)
        create_user_button.place(relx=10,rely=2)
        create_user_button.pack()

