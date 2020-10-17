from tkinter import Button
from Bases import BaseRow, BaseLabel, BaseEntry
import tkinter.ttk as t
from Globals.calculated import fonts
from Static.constants import LINE_MARKERS,FUNCTION,CACHE,CHANGES_CACHE,ID,DATA,TYPE
from Decorators.input_checkers import check_function_input

# VALUE = [id, func,line,color,size]
from Utils.ask_color import ask_color


class FunctionRow(BaseRow):
    def __init__(self, parent, func_value,controller):
        super().__init__(parent, func_value,controller)
        self.type = FUNCTION
        self.text_fun = BaseLabel(self.parent, text="Funkce:")
        self.text_size = BaseLabel(self.parent, text="Vel.:")

        self.entry_fun = BaseEntry(self.parent, width=23)
        self.entry_fun.insert(0, self.value[1])

        self.line_multiselect = t.Combobox(self.parent, values=LINE_MARKERS, state="readonly",
                                           width=5)
        self.line_multiselect.current(LINE_MARKERS.index(self.value[2]))
        self.col_but = Button(self.parent, bg=self.value[3],
                              command=lambda: self.col_but.config(bg=ask_color()),width=10)
        self.entry_size = BaseEntry(self.parent, width=8)
        self.entry_size.insert(0, self.value[4])

        self.text_fun.grid(row=0, column=0)
        self.entry_fun.grid(row=0, column=1, padx=2)
        self.line_multiselect.grid(row=0, column=2, padx=8)
        self.text_size.grid(row=0, column=3)
        self.entry_size.grid(row=0, column=4, padx=4)
        self.col_but.grid(row=0, column=5, padx=4)
        self.del_but.grid(row=0, column=6, padx=4)
        self.save_but.grid(row=0, column=7, padx=4)

    @check_function_input
    def collect_data(self):
        data = self.data_dict()
        id = self.value[0]
        func = self.entry_fun.get()
        line = self.line_multiselect.get()
        color = self.col_but["bg"]
        size = self.entry_size.get()
        data[CACHE] = (id,func,line,color,size)
        data[CHANGES_CACHE][TYPE] = FUNCTION
        data[CHANGES_CACHE][DATA] = (func,line,color,size)
        data[CHANGES_CACHE][ID] = id
        return data