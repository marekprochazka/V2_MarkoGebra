import tkinter.ttk as t
from Static.constants import UPDATE, DATA, ID, ACTION,CACHE,CHANGES_CACHE,ERRORS,MATH
from Globals.variables import Variables as V

class BaseRow:
    def __init__(self, parent, scatter_value):
        self.parent = parent
        self.value = scatter_value

        self.del_but = t.Button(self.parent, text="SMAZAT",
                                command=lambda id=self.value[0]: self.delete_value(id),
                                width=10)
        self.save_but = t.Button(self.parent, text="ULOŽIT",
                                 command=lambda : self.save_changes(self.collect_data),
                                 width=10)
    def collect_data(self):
        pass

    def change_color(self, id):
        print(id)

    def delete_value(self, id):
        print(id)

    def save_changes(self, collector):
        data = collector()
        if data[ERRORS]:
            print("CHYBAAA")
        else:

            for index, value in enumerate(V.cache[0]):
                if value[0] == data[CACHE][0]:
                    V.cache[0][index] = data[CACHE]
            if V.to_animate == MATH:
                if value[0] == data[CACHE][1]:
                    V.cache[1][index] = data[CACHE]
            V.changes_cache.append(data[CHANGES_CACHE])


    def data_dict(self):
        return {CACHE: [], CHANGES_CACHE: {ACTION: UPDATE, DATA: [], ID: ""},ERRORS:[]}
