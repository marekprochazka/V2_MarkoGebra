from Globals.variables import Variables as V
from tkinter import END
class PieUpdate:
    def __init__(self,main):
        self.main = main

    def add_pie_data(self, data, expl=0, entry1=None, entry2=None, cbb=None, error=None):

        try:
            float(data[0])
            V.slices.append(data[0])
            V.activities.append(data[1])
            V.cols.append(data[2])
            V.explode.append(expl)
            if entry1 != None:
                entry1.delete(0, END)
                entry2.delete(0, END)
                cbb.set("")
            V.coordinates_all_list.append([data[1], data[0], data[2]])
            error["text"] = ""

            self.update_table()
        except:
            if entry1 != None:
                entry1.delete(0, END)
                entry2.delete(0, END)
                error["text"] = "Chyba"
                cbb.set("")
            else:
                pass