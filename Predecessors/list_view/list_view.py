from Globals.variables import Variables as V
import tkinter.ttk as t
from Static.constants import MATH, PIE, BAR, NOISE
from . import ScatterRow, FunctionRow, PieRow, BarRow, NoiseRow


# UPDATER (AND CONSTRUCTOR) OF LIST OF INPUTS IN GUI
class ListView:

    def __init__(self, main):
        self.main = main

    def update_list_view(self):
        # CLEARING LIST VIEW
        for child in self.main.frame_scrollable_listView.winfo_children():
            child.destroy()
        # CREATING CONTAINER IN LIST SCROLLABLE FRAME IN GUI FOR EACH VALUE IN CACHE
        list_valueContainers = [t.Label(self.main.frame_scrollable_listView) for _ in range(len(V.cache[0]))]
        # MATH
        if V.currentMethod == MATH:
            # IF IT'S MATH GRAPHING IT IS NECESSARY TO ALSO TAKE SECOND CACHE FOR FUNCTION INPUTS
            list_valueContainers += [t.Label(self.main.frame_scrollable_listView) for _ in
                                     range(len(V.cache[1]))]
            # MAKING ROW FOR EACH SCATTER VALUE
            for i, scatter_value in enumerate(V.cache[0]):
                ScatterRow(list_valueContainers[i], scatter_value, controller=self)
            # MAKING ROW FOR EACH FUNCTION VALUE
            for i, func_value in enumerate(V.cache[1]):
                FunctionRow(list_valueContainers[i + (len(V.cache[0]))], func_value, controller=self)
            # PLACING CONTAINERS TO GRID TO GUI
            self.__place_list_elements(list_valueContainers)
        # BAR
        elif V.currentMethod == BAR:
            # MAKING ROW FOR EACH BAR VALUE
            for i, bar_value in enumerate(V.cache[0]):
                BarRow(list_valueContainers[i], bar_value, controller=self)
            # PLACING CONTAINERS TO GRID TO GUI
            self.__place_list_elements(list_valueContainers)
        # PIE
        elif V.currentMethod == PIE:
            # MAKING ROW FOR EACH PIE VALUE
            for i, pie_value in enumerate(V.cache[0]):
                PieRow(list_valueContainers[i], pie_value, controller=self)
            # PLACING CONTAINERS TO GRID TO GUI
            self.__place_list_elements(list_valueContainers)
        elif V.currentMethod == NOISE:
            # MAKING ROW FOR EACH NOISE VALUE
            for i, noise_value in enumerate(V.cache[0]):
                NoiseRow(list_valueContainers[i], noise_value, controller=self)
            # PLACING CONTAINERS TO GRID TO GUI
            self.__place_list_elements(list_valueContainers)

    def __place_list_elements(self, list_elements):
        for i, val in enumerate(list_elements):
            val.grid(row=i, column=0, padx=5, pady=2, sticky="w")
