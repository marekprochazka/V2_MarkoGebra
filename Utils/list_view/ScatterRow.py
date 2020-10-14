from tkinter import Button

import tkinter.ttk as t
from Globals.calculated import fonts

from Bases import BaseEntry, BaseRow, BaseLabel


# VALUE = [id,x,y,marker,color,size]

class ScatterRow(BaseRow):
    def __init__(self, parent, scatter_value):
        super().__init__(parent, scatter_value)
        self.text_x = BaseLabel(self.parent, text="X:")
        self.text_y = BaseLabel(self.parent, text="Y:")
        self.text_size = BaseLabel(self.parent, text="Vel.:")
        self.entry_x, self.entry_y = BaseEntry(self.parent, width=13), BaseEntry(self.parent, width=13)
        self.entry_x.insert(0, self.value[1])
        self.entry_y.insert(0, self.value[2])

        self.marker_multiselect = t.Combobox(self.parent, values=["aa", "bb"], state="readonly",
                                             width=5)  # TODO fill from constant add command

        self.col_but = Button(self.parent, bg=self.value[4],
                              command=lambda id=self.value[0]: self.change_color(id),
                              width=10)
        self.entry_size = BaseEntry(self.parent, width=8)
        self.entry_size.insert(0, self.value[5])

        self.text_x.grid(row=0, column=0)
        self.entry_x.grid(row=0, column=1)
        self.text_y.grid(row=0, column=2)
        self.entry_y.grid(row=0, column=3)
        self.marker_multiselect.grid(row=0, column=4, padx=8)
        self.text_size.grid(row=0, column=5)
        self.entry_size.grid(row=0, column=6, padx=4)
        self.col_but.grid(row=0, column=7, padx=4)
        self.del_but.grid(row=0, column=8, padx=4)
        self.save_but.grid(row=0, column=9, padx=4)
