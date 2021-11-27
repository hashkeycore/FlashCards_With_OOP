import tkinter as tk
from gui import *

if __name__ == '__main__':
    root = tk.Tk()
    root.title = 'Flashy'
    App(root, bg="#B1DDC6").pack(side="top", fill="both", expand=True)
    root.mainloop()
