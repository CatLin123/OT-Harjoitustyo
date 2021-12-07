'''User interface'''
from tkinter import Tk
from ui.ui import UI
from database_connection import initialize_database


def main():
    '''Main function'''
    window = Tk()
    window.title("Budget app")
    window.geometry("600x400")
    USRI = UI(window)
    USRI.start()
    window.mainloop()

if __name__ == '__main__':

    main()
