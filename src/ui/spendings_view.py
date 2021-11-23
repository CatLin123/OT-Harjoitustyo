import tkinter as tk
from tkinter import *
from tkinter.ttk import Treeview
from entities.spendings import Category
from entities.spendings import Category_list

#from tkinter import ttk #constants



class SpendingsView:
    def __init__(self, root):
        self.root = root
        self.add_frame = tk.Frame(self.root, bg="white")
        self.spending = None
        self.sum = None
        self.categories = Category_list(["Groceries", "Clothes", "Technology"])
        self.category_strings = []
        self.spendings_frame = tk.Frame(self.root, bg="white")
        self.table_frame = tk.Frame(self.spendings_frame, bg="white")
        self.sum = None
        #self.table= tk.Treeview(self.spendings_frame)

        self.initialize() 

    def pack(self):
        self.add_frame.place(relx=0.1, rely=0.6, relheight=0.3, relwidth=0.8)#fill=constants.X

        
        for i in range(self.categories.get_length()):
                category = Entry(self.table_frame)
                summa = Entry(self.table_frame)
                data = self.categories.get_name(i)
                category.insert(END, data)
                summa.insert(END, self.categories.get_sum(i))

                
                category.grid(row=i, column=1)
                summa.grid(row=i, column=2)
        

        self.spendings_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)
        self.table_frame.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)


    

    def create_spending(self):
        sum_content = int(self.sum.get())
        category_content = str(self.spending.get())
        
        
        index = self.categories.get_index(category_content)
 
        self.categories.get_add_summa(index, sum_content)
        self.pack()
        self.sum.delete(0, END)
        

    def initialize(self):
        self.spending = StringVar(self.add_frame)
        self.spending.set(self.categories.get_name(0))

       

        menu = OptionMenu(self.add_frame, self.spending, *["Groceries", "Clothes", "Technology"])
        self.sum = Entry(self.add_frame)
        add = tk.Button(self.add_frame, text="Add", command=self.create_spending)
        
        
        menu.place(relx=0.01, rely=0.8, anchor = W)
        add.place(relx=0.9, rely=0.8, anchor = E)
        self.sum.place(relx=0.5, rely=0.8, anchor = CENTER)


