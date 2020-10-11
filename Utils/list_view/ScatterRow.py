from tkinter import Button

from . import BaseRow
import tkinter.ttk as t
from Globals.calculated import fonts


class ScatterRow(BaseRow):
    def __init__(self, parent, scatter_value):
        super().__init__(parent, scatter_value)
        self.text_x, self.text_y = t.Label(self.parent, text="X:", font=fonts()["SMALL_FONT"]), t.Label(self.parent,
                                                                                                        text="Y:",
                                                                                                        font=fonts()[
                                                                                                            "SMALL_FONT"])
        self.entry_x, self.entry_y = t.Entry(self.parent, justify="center", width=10), t.Entry(self.parent,
                                                                                               justify="center",
                                                                                               width=10)
        self.entry_x.insert(0, self.value[1])
        self.entry_y.insert(0, self.value[2])

        self.marker_multiselect = t.Combobox(self.parent, values=["aa", "bb"], state="readonly",
                                             width=10)  # TODO fill from constant add command

        self.col_but = Button(self.parent, bg=self.value[4],
                              command=lambda id=self.value[0]: self.change_color(id),
                              width=10)
        self.entry_size = t.Entry(self.parent, justify="center", width=8)
        self.entry_size.insert(0, self.value[5])

        self.text_x.grid(row=0, column=0)
        self.entry_x.grid(row=0, column=1)
        self.text_y.grid(row=0, column=2)
        self.entry_y.grid(row=0, column=3)
        self.marker_multiselect.grid(row=0, column=4, padx=8)
        self.col_but.grid(row=0, column=5, padx=4)
        self.entry_size.grid(row=0, column=6, padx=4)
        self.del_but.grid(row=0, column=7, padx=4)
        self.save_but.grid(row=0, column=8, padx=4)
