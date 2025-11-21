import tkinter
from tkinter import ttk

from gmpy2 import gmpy2

from attacks.single_key.abstract_attack import AbstractAttack
from attacks.single_key.solution import Solution

button_style_name = "CustomButtonStyle"



class ButtonMain:

    def __init__(self,
                 root_window,
                 entry_public,
                 entry_modulus,
                 entry_private):
        self.text = "Attack"
        self.init_button_style()

        self.entry_public = entry_public
        self.entry_modulus = entry_modulus
        self.entry_private = entry_private

        self.attack_method = None

        self.button = ttk.Button(
            root_window,
            text = self.text,
            command = self.main_attack,
            style = button_style_name
        )

        self.button.place(x = 20, y = 320)


    def main_attack(self):

        try:
            e = gmpy2.mpz(self.entry_public.entry.get())
            n = gmpy2.mpz(self.entry_modulus.entry.get())
            d = self.attack_method.attack(e, n)

            self.entry_private.print_result(str(d))
        except ValueError:
            self.entry_private.print_result(str("Input Error！"))


    def set_attack_method(self, at: AbstractAttack):
        self.attack_method = at

    @staticmethod
    def init_button_style():
        style = ttk.Style()
        style.configure(button_style_name, font=("Arial", 14, "italic"), padding = (30, 10))
        style.layout(button_style_name, style.layout("TButton"))

class ButtonSolution:

    def __init__(self,
                 root_window,
                 entry_public,
                 entry_modulus,
                 entry_private):
        self.text = "Click me to attack if you know nothing"
        self.init_button_style()

        self.entry_public = entry_public
        self.entry_modulus = entry_modulus
        self.entry_private = entry_private

        self.attack_method = Solution()

        self.button = ttk.Button(
            root_window,
            text = self.text,
            command = self.main_attack,
            style = button_style_name
        )

        self.button.place(x = 300, y = 400)


    def main_attack(self):

        try:
            e = gmpy2.mpz(self.entry_public.entry.get())
            n = gmpy2.mpz(self.entry_modulus.entry.get())
            d = self.attack_method.attack(e, n)

            self.entry_private.print_result(str(d))
        except ValueError:
            self.entry_private.print_result(str("Input Error！"))


    @staticmethod
    def init_button_style():
        style = ttk.Style()
        style.configure(button_style_name, font=("Mircosoft YaHei", 14, "bold"), padding = (30, 10))
        style.layout(button_style_name, style.layout("TButton"))











