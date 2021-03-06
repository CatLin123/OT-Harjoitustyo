'''User interface'''
from ui.spendings_view import SpendingsView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView

class UI:
    '''Show user interface'''
    def __init__(self,root):
        self.root = root
        self.current_view = None

    def start(self):
        '''Start'''
        self.show_login_view()
        #self.show_spendings_view()

    def hide_current_view(self):
        '''Hide current view'''
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_login_view(self):
        '''Show login view'''
        self.hide_current_view()
        self.current_view = LoginView(self.root, self.show_spendings_view, self.show_create_user_view)
        self.current_view.pack()

    def show_spendings_view(self):
        '''Show spendings view'''
        self.hide_current_view()
        self.current_view = SpendingsView(self.root)
        self.current_view.pack()

    def show_create_user_view(self):
        '''Show create user view'''
        self.hide_current_view()
        self.current_view = CreateUserView(self.root, self.show_login_view)
        self.current_view.pack()
        