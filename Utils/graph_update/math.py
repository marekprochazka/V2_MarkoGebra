from Globals.variables import Variables as V
from tkinter import END
from Static.constants import FUNCTION_ALLOWED_MARKS, ACTION, CREATE, ID, DATA, TYPE, SCATTER, FUNCTION
import numpy as np
from Utils.uuid import generate_uuid


class MathUpdate:
    def __init__(self, main):
        self.main = main

    # FUNCTIONS, THAT IS CALLED WHEN THE MATH GRAPH IS UPDATED FROM FE

    # SCATTER INPUT
    def add_point_scatter(self, x, y, marker=".", color="blue", size="1", error=None, entry1=None, entry2=None):
        try:
            # VALID INPUT CHECK
            x = int(x)
            y = int(y)

            # UPDATING LIMITS (IF NEEDED)
            if V.is_auto_update:
                self.main.auto_update_limits_by_scatter_input(x, y)

            # GENERATING UUID FOR IDENTIFYING, APPENDING TO CACHES
            uuid = generate_uuid()
            V.cache[0].append((uuid, x, y, marker, color, size))
            V.changes_cache.append({ACTION: CREATE, DATA: (x, y, marker, color, size), ID: uuid, TYPE: SCATTER})

            # CLEARING ENTRIES, UPDATING TABLE
            if error != None:
                error["text"] = ""
                entry1.delete(0, END)
                entry2.delete(0, END)
                self.main.update_list_view()
        except:
            if error != None:
                error["text"] = "chyba"
                entry1.delete(0, END)
                entry2.delete(0, END)

    # FUNCTION INPUT
    def add_plot_from_function(self, function: str, line="solid", color="blue", size="1", error=None, entry=None):
        # VALID INPUT CHECK
        is_all_fine = True
        for char in function:
            if char not in FUNCTION_ALLOWED_MARKS:
                is_all_fine = False

        if is_all_fine:
            function = function.replace("s", "sin")
            function = function.replace("c", "cos")
            function = function.replace("t", "tan")
            function = function.replace("p", "pi")
            y = function

            # GENERATING UUID FOR IDENTIFING, APPENDING TO CACHES
            uuid = generate_uuid()
            V.cache[1].append((uuid, y, line, color, size))
            V.changes_cache.append({ACTION: CREATE, DATA: (y, line, color, size), ID: uuid, TYPE: FUNCTION})

            # CLEARING ENTRIES, UPDATING TABLE
            if error != None:
                error["text"] = ""
                entry.delete(0, END)
            self.main.update_list_view()
        else:
            if error != None:
                entry.delete(0, END)

                error["text"] = "chyba"
