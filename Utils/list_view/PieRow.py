from tkinter import Button

from . import BaseRow
import tkinter.ttk as t
from Globals.calculated import fonts

from Bases.BaseEntry import BaseEntry


# VALUE = [id,slice,activity,color,explode]
class PieRow(BaseRow):
    def __init__(self, parent, pie_value):
        super().__init__(parent, pie_value)
        self.text_slice = t.Label(self.parent, text="Množství:", font=fonts()["SMALL_FONT"])
        self.text_activity = t.Label(self.parent, text="Název:", font=fonts()["SMALL_FONT"])
        self.text_explode = t.Label(self.parent, text="Výstup:", font=fonts()["SMALL_FONT"])

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
