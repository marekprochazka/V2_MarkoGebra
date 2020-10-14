from tkinter import Button

from . import BaseRow
import tkinter.ttk as t
from Globals.calculated import fonts


# VALUE = [id, func,line,color,size]
class FunctionRow(BaseRow):
    def __init__(self, parent, func_value):
        super().__init__(parent, func_value)
        self.text_fun = t.Label(self.parent, text="Funkce:", font=fonts()["SMALL_FONT"])
        self.text_size = t.Label(self.parent, text="Vel.:", font=fonts()["SMALL_FONT"])

        self.entry_fun = t.Entry(self.parent, justify="center", width=23)
        self.entry_fun.insert(0, self.value[1])

        self.line_multiselect = t.Combobox(self.parent, values=["aa", "bb"], state="readonly",
                                           width=5)  # TODO fill from constant add command
        self.col_but = Button(self.parent, bg=self.value[3],
                              command=lambda id=self.value[0]: self.change_color(id), width=10)
        self.entry_size = t.Entry(self.parent, justify="center", width=8)
        self.entry_size.insert(0, self.value[4])

        self.text_fun.grid(row=0, column=0)
        self.entry_fun.grid(row=0, column=1, padx=2)
        self.line_multiselect.grid(row=0, column=2, padx=8)
        self.text_size.grid(row=0, column=3)
        self.entry_size.grid(row=0, column=4, padx=4)
        self.col_but.grid(row=0, column=5, padx=4)
        self.del_but.grid(row=0, column=6, padx=4)
        self.save_but.grid(row=0, column=7, padx=4)
