from Globals.variables import Variables as V
from tkinter import END
from Utils.uuid import generate_uuid
from Static.constants import ACTION, CREATE, ID, DATA


class BarUpdate:
    def __init__(self, main):
        self.main = main

    # FUNCTION, THAT IS CALLED WHEN THE BAR GRAPH IS UPDATED FROM FE
    def add_bar_data(self, name, value, color, entry1, entry2, cbb, error):
        try:
            # INPUT CHECK
            float(value)
            # GENERATING UUID FOR IDENTIFYING, APPENDING TO CACHES
            uuid = generate_uuid()
            V.cache[0].append((uuid, name, value, color, 0.8))
            V.changes_cache.append({ACTION: CREATE, DATA: (name, value, color, 0.8), ID: uuid})

            # EMPTYING ENTRIES, UPDATING TABLE
            entry1.delete(0, END)
            entry2.delete(0, END)
            cbb.set("")
            error["text"] = ""

            self.main.update_list_view()
        except:
            # EMPTYING ENTRIES
            entry1.delete(0, END)
            entry2.delete(0, END)
            error["text"] = "Chyba"
            cbb.set("")
