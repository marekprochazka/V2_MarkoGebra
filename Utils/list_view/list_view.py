from Globals.variables import Variables as V
import tkinter.ttk as t
from Globals.calculated import fonts
from tkinter import LEFT, END, Button
from Static.constants import MATH, PIE, BAR, NOISE
from . import ScatterRow, FunctionRow, PieRow, BarRow


# UPDATER OF LIST GUI
# TODO WILL BE REFACTORED SOON
class ListView:

    def __init__(self, main):
        self.main = main

    def update_list_view(self):
        for child in self.main.list_view_scrollable_frame.winfo_children():
            child.destroy()
        list_elements = [t.Label(self.main.list_view_scrollable_frame) for _ in range(len(V.cache[0]))]
        if V.to_animate == MATH:
            list_elements += [t.Label(self.main.list_view_scrollable_frame) for _ in
                                   range(len(V.cache[1]))]
            for i, scatter_value in enumerate(V.cache[0]):
                ScatterRow(list_elements[i], scatter_value, controller=self)
            for i, func_value in enumerate(V.cache[1]):
                FunctionRow(list_elements[i + (len(V.cache[0]))], func_value,controller=self)
            self.__place_list_elements(list_elements)

        elif V.to_animate == BAR:
            for i, bar_value in enumerate(V.cache[0]):
                BarRow(list_elements[i],bar_value,controller=self)
            self.__place_list_elements(list_elements)

        elif V.to_animate == PIE:
            for i, pie_value in enumerate(V.cache[0]):
                PieRow(list_elements[i], pie_value,controller=self)
            self.__place_list_elements(list_elements)

    def __place_list_elements(self, list_elements):
        for i, val in enumerate(list_elements):
            val.grid(row=i, column=0, padx=5, pady=2, sticky="w")
