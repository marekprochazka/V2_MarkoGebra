from tkinter import Button
from Bases import BaseEntry, BaseRow, BaseLabel
from Decorators.input_checkers import check_bar_input
from Static.constants import CACHE, CHANGES_CACHE, DATA, ID
from Utils.ask_color import ask_color

# VALUE = [id,name,value,color,width]

class BarRow(BaseRow):
    def __init__(self, parent, pie_value,controller):
        super().__init__(parent, pie_value,controller)
        self.text_name = BaseLabel(self.parent, text="Název:")
        self.text_value = BaseLabel(self.parent, text="Množstvý:")
        self.text_width = BaseLabel(self.parent, text="Šířka:")

        self.entry_name = BaseEntry(self.parent, width=8)
        self.entry_name.insert(0, self.value[1])
        self.entry_value = BaseEntry(self.parent, width=13)
        self.entry_value.insert(0, self.value[2])
        self.entry_width = BaseEntry(self.parent, width=8)
        self.entry_width.insert(0, self.value[4])

        self.col_but = Button(self.parent, bg=self.value[3],
                              command=lambda: self.col_but.config(bg=ask_color()),
                              width=10)

        self.text_value.grid(row=0, column=0)
        self.entry_value.grid(row=0, column=1, padx=2)
        self.text_name.grid(row=0, column=2)
        self.entry_name.grid(row=0, column=3, padx=2)
        self.text_width.grid(row=0, column=4)
        self.entry_width.grid(row=0, column=5, padx=2)
        self.col_but.grid(row=0, column=6, padx=3)
        self.del_but.grid(row=0, column=7, padx=3)
        self.save_but.grid(row=0, column=8, padx=3)

    @check_bar_input
    def collect_data(self):
        data = self.data_dict()
        id = self.value[0]
        name = self.entry_name.get()
        value = self.entry_value.get()
        color = self.col_but["bg"]
        width = self.entry_width.get()
        data[CACHE] = (id,name,value,color,width)
        data[CHANGES_CACHE][DATA] = (name,value,color,width)
        data[CHANGES_CACHE][ID] = id
        return data