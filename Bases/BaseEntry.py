from tkinter.ttk import Entry
import tkinter as tk

# ADDITION TO NORMAL TK ENTRY, JUSTIFY CENTER IS USED ON EVERY ENTRY IN CODE
class BaseEntry(Entry):
    def __init__(self, parent, justify="center", numbers=False, **kwargs):
        if numbers:
            super().__init__(parent, justify=justify, **kwargs)
            self.vcmd_digit = (self.register(self.__is_digit_callback))
            super().__init__(parent,justify=justify,validate='all',validatecommand=(self.vcmd_digit, '%P'), **kwargs)
        else:
            super().__init__(parent, justify=justify, **kwargs)

    def __is_digit_callback(self ,P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False