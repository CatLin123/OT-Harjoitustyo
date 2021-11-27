'''Spendingsview'''
import tkinter as tk
from entities.spendings import CategoryList

class SpendingsView:
    '''Spendingsview'''
    def __init__(self, root):
        '''Spendingsview'''
        self.root = root
        self.add_frame = tk.Frame(self.root, bg="white")
        self.spending = None
        self.sum = None
        self.categories = CategoryList(["Groceries", "Clothes", "Technology"])
        self.spendings_frame = tk.Frame(self.root, bg="white")
        self.table_frame = tk.Frame(self.spendings_frame, bg="white")
        self.initialize()

    def pack(self):
        '''Spendingsview'''
        self.add_frame.place(relx=0.1, rely=0.6, relheight=0.3, relwidth=0.8)#fill=constants.X

        for i in range(self.categories.get_length()):
            category = tk.Entry(self.table_frame)
            summa = tk.Entry(self.table_frame)
            data = self.categories.get_name(i)
            category.insert(tk.END, data)
            summa.insert(tk.END, self.categories.get_sum(i))
            category.grid(row=i, column=1)
            summa.grid(row=i, column=2)

        self.spendings_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)
        self.table_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)

    def create_spending(self):
        '''Spendingsview'''
        sum_content = float(self.sum.get())
        category_content = str(self.spending.get())
        index = self.categories.get_index(category_content)
        self.categories.get_add_summa(index, sum_content)
        self.pack()
        self.sum.delete(0,tk.END)
          
    def initialize(self):
        '''Spendingsview'''
        self.spending = tk.StringVar(self.add_frame)
        self.spending.set(self.categories.get_name(0))
        menu = tk.OptionMenu(self.add_frame, self.spending, *["Groceries", "Clothes", "Technology"])
        self.sum = tk.Entry(self.add_frame)
        add = tk.Button(self.add_frame, text="Add", command=self.create_spending)          
        menu.place(relx=0.01, rely=0.8, anchor = tk.W)
        add.place(relx=0.9, rely=0.8, anchor = tk.E)
        self.sum.place(relx=0.5, rely=0.8, anchor = tk.CENTER)
