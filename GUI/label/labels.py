import tkinter
from tkinter import ttk

class LabelTitle:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="RSAHacker",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 20, y = 20)

class LabelPublicKey:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="Public Key",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 20, y = 80)

class LabelModulus:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="Modulu",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 20, y = 200)

class LabelPrivateKey:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="Private Key",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 20, y = 390)

class LabelAttackSelector:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="Attack Method",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 250, y = 80)

class LabelDefectSelector:
    def __init__(self, root_window):
        self.root_window = root_window
        self.label = tkinter.Label(
            self.root_window,
            text="Key Defect",
            font=("Consolas", 21, "bold"),
            bg="light blue",
            fg="black"
        )

        self.label.place(x = 520, y = 80)