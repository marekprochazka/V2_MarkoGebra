from Globals.variables import Variables as V
from tkinter import END
from Static.constants import FUNCTION_ALLOWED_MARKS
import numpy as np

class MathUpdate:
    def __init__(self,main):
        self.main = main

    def add_point_scatter(self, x, y, marker=".", color="blue", size="1", error=None, entry1=None, entry2=None):
        try:
            x = int(x)
            y = int(y)
            if x > V.lim1:
                V.lim1 = x
            if x < V.lim2:
                V.lim2 = x
            if y > V.lim1:
                V.lim1 = y
            if y < V.lim2:
                V.lim2 = y
            if [x, y] not in V.coordinates_scatter:
                V.coordinates_scatter.append([x, y, marker, color, size])
                V.coordinates_all_list.append([[x, y], marker, color, size])
                if error != None:
                    error["text"] = ""
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    self.main.update_table()
        except:
            if error != None:
                error["text"] = "chyba"
                entry1.delete(0, END)
                entry2.delete(0, END)

    def add_plot_from_function(self, function: str, line="solid", color="blue", size="1", error=None, entry=None):
        is_all_fine = True
        for char in function:
            if char not in FUNCTION_ALLOWED_MARKS:
                is_all_fine = False

        if is_all_fine:
            function = function.replace("s", "sin")
            function = function.replace("c", "cos")
            function = function.replace("t", "tan")
            function = function.replace("p", "pi")
            x = np.arange(V.lim2, V.lim1, 0.5)
            y = function

            checnk = True
            if len(V.coordinates_plot) >= 1:
                for val in V.coordinates_plot:
                    if val[1] == y:
                        checnk = False
            if checnk:
                V.coordinates_plot.append([x, y, line, color, size, function])
                V.coordinates_all_list.append([["f(x)", function], line, color, size])
            if error != None:
                error["text"] = ""
                entry.delete(0, END)
            self.main.update_table()
        else:
            if error != None:
                entry.delete(0, END)

                error["text"] = "chyba"