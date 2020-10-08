from Globals.variables import Variables as V
import tkinter.ttk as t
from Globals.calculated import fonts
from tkinter import LEFT
from Static.constants import MATH,PIE,BAR,NOISE

#UPDATER OF LIST GUI
#TODO WILL BE REFACTORED SOON
class UpdateTable:
    def __init__(self, main):
        self.main = main

    def update_table(self):

        for child in self.main.scrollable_frame.winfo_children():
            for child_of_child in child.winfo_children():
                child_of_child.destroy()
        counter = 0
        for index, parent in enumerate(self.main.scrollable_frame.winfo_children()):
            try:
                if V.to_animate == MATH:
                    full_list = V.cache[0] + V.cache[1] #WIP
                    t.Label(parent,
                            text=f"{counter}. {full_list[index][0]}",
                            font=fonts()["SMALL_FONT"],
                            justify=LEFT, anchor="w").grid(row=counter, column=0, sticky="we")

                elif V.to_animate == BAR or V.to_animate == PIE:
                    t.Label(parent,
                            text=f"{counter}. Název: {V.cache[index][1]}; Hodnota: {V.cache[index][2]}; Barva: {V.cache[index][3]}",
                            font=fonts()["SMALL_FONT"],
                            justify=LEFT, anchor="w").grid(row=counter, column=0, sticky="we")
                elif V.to_animate == 4: #TODO
                    t.Label(parent,
                            text=f"{counter}. Množství: {V.coordinates_all_list[index][0]}; Rozptyl: {V.coordinates_all_list[index][1]}; Značka: {V.coordinates_all_list[index][2]}; Barva: {V.coordinates_all_list[index][3]}; Velikost: {V.coordinates_all_list[index][4]}",
                            font=fonts()["SMALL_FONT"],
                            justify=LEFT, anchor="w").grid(row=counter, column=0, sticky="we")

                counter += 1

            except IndexError:
                pass
