from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Budget app")
    window.geometry("600x400")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()