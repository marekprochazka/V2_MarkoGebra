from Globals.variables import Variables as V
import tkinter.ttk as t
from Globals.calculated import fonts
from tkinter import LEFT
from Static.constants import MATH, PIE, BAR, NOISE


# UPDATER OF LIST GUI
# TODO WILL BE REFACTORED SOON
class UpdateTable:
    def __init__(self, main):
        self.main = main

    def update_table(self):
        self.list_elements_scatter = [t.Label(self.main.list_view_scrollable_frame) for _ in range(len(V.cache[0]))]
        self.elements_stack = []
        if V.to_animate == MATH:
            for i,scatter_value in enumerate(V.cache[0]):
                self.elements_stack.append(t.Label(self.list_elements_scatter[i],
                                                  text=f"sc:{scatter_value[1]}:{scatter_value[2]}", ).grid(row=0,column=0))
                self.elements_stack.append(t.Label(self.list_elements_scatter[i],
                                                   text=f"sc:{scatter_value[1]}:{scatter_value[2]}", ).grid(row=0,column=1))
            for i, val in enumerate(self.list_elements_scatter):
                val.grid(row=i, column=0, padx=20, sticky="w")

    def dummy_func(self, vaalue):
        print(vaalue)
