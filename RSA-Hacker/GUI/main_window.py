import tkinter as tk

import GUI

import sv_ttk

from GUI.combobox.treeviews import AttackSelectorTreeView, DefectSelectorTreeView
from GUI.entry.entries import EntryPublicKey, EntryModulus, EntryPrivateKey
from button.buttons import ButtonMain, ButtonSolution
from GUI.label.labels import LabelTitle, LabelPublicKey, LabelModulus, LabelPrivateKey, LabelAttackSelector, \
    LabelDefectSelector


class MainWindow:
    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.title("RSAHacker")
        self.root_window.geometry("800x500")

        self.entry_public_key = EntryPublicKey(self.root_window)
        self.entry_modulus = EntryModulus(self.root_window)
        self.entry_private_key = EntryPrivateKey(self.root_window)

        # self.entry_public_key.entry.insert(0, "5")
        # self.entry_modulus.entry.insert(0, "35")

        self.button_main = ButtonMain(self.root_window,
                                      entry_modulus=self.entry_modulus,
                                      entry_public=self.entry_public_key,
                                      entry_private=self.entry_private_key)

        self.button_solution = ButtonSolution(self.root_window,
                                      entry_modulus=self.entry_modulus,
                                      entry_public=self.entry_public_key,
                                      entry_private=self.entry_private_key)

        self.attack_selector_treeview = AttackSelectorTreeView(self.root_window,
                                                               self.button_main)
        self.defect_selector_treeview = DefectSelectorTreeView(self.root_window,
                                                               self.button_main)
        self.label_title = LabelTitle(self.root_window)
        self.label_public_key = LabelPublicKey(self.root_window)
        self.label_modulus = LabelModulus(self.root_window)
        self.label_private_key = LabelPrivateKey(self.root_window)
        self.label_attack_selector = LabelAttackSelector(self.root_window)
        self.label_defect_selector = LabelDefectSelector(self.root_window)



    def run(self):
        sv_ttk.set_theme("light")
        self.root_window.mainloop()