import tkinter
from tkinter import ttk
import re

from attacks.attack_enum import AttackEnum
from attacks.defect_enum import DefectEnum


class AttackSelectorTreeView:
    def __init__(self, root_window, attack_button):
        self.root_window = root_window
        self.attack_button = attack_button

        self.treeview = ttk.Treeview(root_window,
                                     columns="attack",
                                     show="headings")
        self.treeview.heading("attack", text = "Attack Method")

        for attack in AttackEnum:
            self.treeview.insert("", "end", values=attack.get_instance().name)

        self.treeview.bind("<<TreeviewSelect>>", self.on_selection)
        self.treeview.place(x = 250, y = 150)


    def on_selection(self, event):
        selection = self.treeview.selection()[0]
        item_select = self.treeview.item(selection, "values")
        item = item_select.__getitem__(0)

        at = None
        for attack in AttackEnum:
            if attack.get_instance().name == item:
                at = attack.get_instance()

        self.attack_button.set_attack_method(at)


class DefectSelectorTreeView:
    def __init__(self, root_window, attack_button):
        self.root_window = root_window
        self.attack_button = attack_button

        self.treeview = ttk.Treeview(root_window,
                                     columns="defect",
                                     show="headings")
        self.treeview.heading("defect", text = "Key Defect")

        for defect in DefectEnum:
            self.treeview.insert("", "end", values=defect.get_name())

        self.treeview.bind("<<TreeviewSelect>>", self.on_selection)
        self.treeview.place(x = 520, y = 150)


    def on_selection(self, event):
        selection = self.treeview.selection()[0]
        item_select = self.treeview.item(selection, "values")
        item = item_select.__getitem__(0)

        at = None
        for attack in DefectEnum:
            if attack.get_name() == item:
                at = attack.get_instance()

        self.attack_button.set_attack_method(at)

def clean_string(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", "", text)






