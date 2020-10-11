from Globals.variables import Variables as V
import tkinter.ttk as t
from Globals.calculated import fonts
from tkinter import LEFT, END, Button
from Static.constants import MATH, PIE, BAR, NOISE


# UPDATER OF LIST GUI
# TODO WILL BE REFACTORED SOON
class ListView:

    def __init__(self, main):
        self.main = main

    def update_list_view(self):
        self.list_elements_scatter = [t.Label(self.main.list_view_scrollable_frame) for _ in range(len(V.cache[0]))]
        if V.to_animate == MATH:
            for i, scatter_value in enumerate(V.cache[0]):
                self.__create_scatter_row(self.list_elements_scatter[i], scatter_value)
            for i, val in enumerate(self.list_elements_scatter):
                val.grid(row=i, column=0, padx=5, sticky="w")

    def __create_scatter_row(self, parent, scatter_value):
        text_x, text_y = t.Label(parent, text="X:", font=fonts()["SMALL_FONT"]), t.Label(parent, text="Y:",
                                                                                         font=fonts()["SMALL_FONT"])
        entry_x, entry_y = t.Entry(parent, justify="center", width=10), t.Entry(parent, justify="center", width=10)
        entry_x.insert(0, scatter_value[1])
        entry_y.insert(0, scatter_value[2])

        marker_multiselect = t.Combobox(parent, values=["aa", "bb"], state="readonly", width=10)

        col_but = Button(parent, bg=scatter_value[4], command=lambda id=scatter_value[0]: self.__change_color(id),
                         width=10)
        del_but = t.Button(parent, text="DELETE", command=lambda id=scatter_value[0]: self.__delete_value(id),
                           width=10)
        save_but = t.Button(parent, text="SAVE", command=lambda id=scatter_value[0]: self.__save_changes(id),
                            width=10)

        text_x.grid(row=0, column=0)
        entry_x.grid(row=0, column=1)
        text_y.grid(row=0, column=2)
        entry_y.grid(row=0, column=3)
        marker_multiselect.grid(row=0, column=4, padx=8)
        col_but.grid(row=0, column=5, padx=4)
        del_but.grid(row=0, column=6, padx=4)
        save_but.grid(row=0, column=7, padx=4)

    def __change_color(self, id):
        print(id)

    def __delete_value(self, id):
        print(id)

    def __save_changes(self, id):
        print(id)
