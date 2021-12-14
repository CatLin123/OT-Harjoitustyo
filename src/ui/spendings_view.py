'''Spendingsview'''
import tkinter as tk
from services.budget_service import budget_service, UsernameExistsError

class SpendingsView:
    '''Spendingsview'''
    def __init__(self, root):
        '''Spendingsview'''
        self.root = root
        self.add_frame = tk.Frame(self.root, bg="white")
        self.spending = None
        self.sum = None
        self.spendings_frame = tk.Frame(self.root, bg="white")
        self.table_frame = tk.Frame(self.spendings_frame, bg="white")
        self.total_frame = tk.Frame(self.table_frame, bg="white")
        self.spendings_list = budget_service.get_columns_spendings()
        self.total_list = budget_service.get_columns_users()
        self.initialize()
          
    
    def pack(self):
        self.add_frame.place(relx=0.1, rely=0.6, relheight=0.3, relwidth=0.8)
        for i in range(len(self.spendings_list)-1):
            category = tk.Entry(self.table_frame)
            summa = tk.Entry(self.table_frame)
            category.insert(tk.END, self.spendings_list[i+1])
            summa.insert(tk.END, budget_service.get_sum(self.spendings_list[i+1]))
            category.grid(row=i, column=1)
            summa.grid(row=i, column=2)
        for i in range(len(self.total_list)-2):
            category = tk.Entry(self.total_frame)
            summa = tk.Entry(self.total_frame)
            category.insert(tk.END, self.total_list[i+2])
            summa.insert(tk.END, budget_service.get_monthly(self.total_list[i+2]))
            category.grid(row=i, column=1)
            summa.grid(row=i, column=2)
        self.spendings_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)
        self.table_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)
        self.total_frame.place(relx=0, rely=0.7, relheight=0.3, relwidth=1)

    def create_spending(self):
        '''Spendingsview''' 
        sum_content = float(self.sum.get())
        category_content = str(self.spending.get())
        budget_service.create_spending(sum_content, category_content)
        self.sum.delete(0,tk.END)
        self.pack()

    def initialize(self):
        '''Spendingsview'''
        self.spending = tk.StringVar(self.add_frame)
      
        menu = tk.OptionMenu(self.add_frame, self.spending, *["Groceries", "Clothes", "Technology","Other"])
        self.sum = tk.Entry(self.add_frame)
        add = tk.Button(self.add_frame, text="Add", command=self.create_spending)          
        menu.place(relx=0.01, rely=0.8, anchor = tk.W)
        add.place(relx=0.9, rely=0.8, anchor = tk.E)
        self.sum.place(relx=0.5, rely=0.8, anchor = tk.CENTER)
        self.add_frame.pack()
