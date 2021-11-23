from ui.spendings_view import SpendingsView
from tkinter import *

class UI:
    def __init__(self,root):
        self.root = root

    def start(self):
        self.show_spendings_view()

    
    def show_spendings_view(self):
        self.current_view = SpendingsView(self.root)
        self.current_view.pack()
