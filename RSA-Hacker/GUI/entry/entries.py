import tkinter
from tkinter import ttk



class EntryPublicKey:
    def __init__(self, root_window):

        self.style = ttk.Style()
        self.style.configure("TEntry", font=("Arial", 20))
        self.root_window = root_window
        self.entry = ttk.Entry(root_window)

        self.entry.place(x = 20, y = 140)

class EntryModulus:
    def __init__(self, root_window):

        self.style = ttk.Style()
        self.style.configure("TEntry", font=("Arial", 20))
        self.root_window = root_window
        self.entry = ttk.Entry(root_window)

        self.entry.place(x = 20, y = 260)

class EntryPrivateKey:
    def __init__(self, root_window):

        self.style = ttk.Style()
        self.style.configure("TEntry", font=("Arial", 20))
        self.root_window = root_window
        self.entry = ttk.Entry(root_window)

        self.entry.place(x = 20, y = 450)

    def print_result(self, result):

        self.entry.delete(0, "end")
        self.entry.insert(0, result)