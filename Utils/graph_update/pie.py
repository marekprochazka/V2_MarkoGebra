from Globals.variables import Variables as V
from tkinter import END
from Utils.uuid import generate_uuid

class PieUpdate:
    def __init__(self,main):
        self.main = main

    def add_pie_data(self, data, expl=0, entry1=None, entry2=None, cbb=None, error=None):

        try:
            float(data[0])

            V.cache[0].append(generate_uuid(),data[0],data[1],data[2],expl)

            if entry1 != None:
                entry1.delete(0, END)
                entry2.delete(0, END)
                cbb.set("")

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