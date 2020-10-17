from tkinter import Button

import tkinter.ttk as t
from Globals.calculated import fonts

from Bases import BaseEntry, BaseRow, BaseLabel


# VALUE = [id,slice,activity,color,explode]
class PieRow(BaseRow):
    def __init__(self, parent, pie_value,controller):
        super().__init__(parent, pie_value,controller)
        self.text_slice = BaseLabel(self.parent, text="Množství:")
        self.text_activity = BaseLabel(self.parent, text="Název:")
        self.text_explode = BaseLabel(self.parent, text="Výstup:")

        self.entry_slice = BaseEntry(self.parent, width=8)
        self.entry_slice.insert(0, self.value[1])
        self.entry_activity = BaseEntry(self.parent, width=12)
        self.entry_activity.insert(0, self.value[2])
        self.entry_explode = BaseEntry(self.parent, width=8)
        self.entry_explode.insert(0, self.value[4])

        self.col_but = Button(self.parent, bg=self.value[3],
                              command=lambda id=self.value[0]: self.change_color(id),
                              width=10)

        self.text_slice.grid(row=0, column=0)
        self.entry_slice.grid(row=0, column=1, padx=2)
        self.text_activity.grid(row=0, column=2)
        self.entry_activity.grid(row=0, column=3, padx=2)
        self.text_explode.grid(row=0, column=4)
        self.entry_explode.grid(row=0, column=5, padx=2)
        self.col_but.grid(row=0, column=6, padx=3)
        self.del_but.grid(row=0, column=7, padx=3)
        self.save_but.grid(row=0, column=8, padx=3)
