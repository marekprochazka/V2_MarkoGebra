from Globals.variables import Variables as V
import tkinter.ttk as t
from Globals.calculated import fonts
from tkinter import LEFT, END, Button
from Static.constants import MATH, PIE, BAR, NOISE
from . import ScatterRow, FunctionRow


# UPDATER OF LIST GUI
# TODO WILL BE REFACTORED SOON
class ListView:

    def __init__(self, main):
        self.main = main

    def update_list_view(self):
        self.list_elements_scatter = [t.Label(self.main.list_view_scrollable_frame) for _ in range(len(V.cache[0]))]
        if V.to_animate == MATH:
            self.list_elements_scatter += [t.Label(self.main.list_view_scrollable_frame) for _ in
                                           range(len(V.cache[1]))]
            for i, scatter_value in enumerate(V.cache[0]):
                ScatterRow(self.list_elements_scatter[i], scatter_value)
            for i, func_value in enumerate(V.cache[1]):
                FunctionRow(self.list_elements_scatter[i+(len(V.cache[0]))], func_value)
            for i, val in enumerate(self.list_elements_scatter):
                val.grid(row=i, column=0, padx=5, sticky="w")
