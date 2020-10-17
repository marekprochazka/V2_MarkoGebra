from tkinter import Button

import tkinter.ttk as t
from Globals.calculated import fonts

from Bases import BaseEntry, BaseRow, BaseLabel
from Static.constants import DATA, ID, TYPE, SCATTER,CHANGES_CACHE,CACHE,ERRORS, POINT_MARKERS
from Decorators.input_checkers import check_scatter
from Globals.variables import Variables as V
from Utils.ask_color import ask_color

# VALUE = [id,x,y,marker,color,size]

class ScatterRow(BaseRow):
    def __init__(self, parent, scatter_value,controller):
        super().__init__(parent, scatter_value,controller)
        self.type = SCATTER
        self.text_x = BaseLabel(self.parent, text="X:")
        self.text_y = BaseLabel(self.parent, text="Y:")
        self.text_size = BaseLabel(self.parent, text="Vel.:")
        self.entry_x, self.entry_y = BaseEntry(self.parent, width=13), BaseEntry(self.parent, width=13)
        self.entry_x.insert(0, self.value[1])
        self.entry_y.insert(0, self.value[2])

        self.marker_multiselect = t.Combobox(self.parent, values=POINT_MARKERS, state="readonly",
                                             width=5)
        self.marker_multiselect.current(POINT_MARKERS.index(self.value[3]))
        self.col_but = Button(self.parent, bg=self.value[4],
                              command=lambda: self.col_but.config(bg=ask_color()),
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

    @check_scatter
    def collect_data(self):
        data = self.data_dict()
        id = self.value[0]
        x = self.entry_x.get()
        y = self.entry_y.get()
        marker = self.marker_multiselect.get()
        color = self.col_but["bg"]
        size = self.entry_size.get()
        data[CACHE] = [id, x, y, marker, color, size]
        data[CHANGES_CACHE][TYPE] = SCATTER
        data[CHANGES_CACHE][DATA] = [x, y, marker, color, size]
        data[CHANGES_CACHE][ID] = id
        return data



