from tkinter import Frame, Label, Button, END
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import MATH, CACHE, CHANGES_CACHE, TYPE, SCATTER, DATA, ID, CREATE, FUNCTION
from Bases import BaseEntry, BaseLabel
from Utils.ask_color import ask_color
from Static.constants import DATA_UPDATE_DICT
from Utils.uuid import generate_uuid
from Decorators.input_checkers import check_function_input, check_scatter_input

# GUI OF MATH INPUTS
class Mathematical(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = MATH
        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # SCATTER INPUT PART
        self.labelX = BaseLabel(self, text="X:")
        self.labelY = BaseLabel(self, text="Y:")

        self.labelX.grid(row=0, column=0)
        self.labelY.grid(row=0, column=2)

        self.EntryX = BaseEntry(self)
        self.EntryY = BaseEntry(self)

        self.EntryX.grid(row=0, column=1, sticky="we")
        self.EntryY.grid(row=0, column=3, sticky="we")

        self.colorButtonScatter = Button(self, bg="blue", width=15,
                                         command=lambda: self.__set_value_color(self.colorButtonScatter))
        self.colorButtonScatter.grid(row=0, column=4, sticky="we", padx=2)

        self.placeButtonScatter = t.Button(self, text="Vložit",
                                           command=lambda: self.__update_data_scatter())
        self.placeButtonScatter.grid(row=0, column=5, sticky="we")

        # FUNCTION INPUT PART
        self.labelFun = BaseLabel(self, text="f(x):")
        self.labelFun.grid(row=1, column=0)

        self.EntryFun = BaseEntry(self)

        self.EntryFun.grid(row=1, column=1, columnspan=3, sticky="we")

        self.colorButtonFunc = Button(self, bg="blue", width=15)
        self.colorButtonFunc.grid(row=1, column=4, sticky="we", padx=2)

        self.placeButtonPlot = t.Button(self, text="Odložit",
                                        command=lambda: self.__update_data_function)

        self.placeButtonPlot.grid(row=1, column=5, sticky="we", pady=20)

        self.ErrorWarning = Label(self, text="", font=fonts()["SMALL_FONT"], fg="red")
        self.ErrorWarning.grid(row=2, column=2)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(5, weight=2)

    def __update_data_scatter(self):
        from Utils.update_data import update_data
        update_data(self.__collect_scatter(),self.controller.update_list_view)
        self.EntryX.delete(0,END)
        self.EntryY.delete(0,END)

    def __update_data_function(self):
        from Utils.update_data import update_data
        update_data(self.__collect_function(), self.controller.update_list_view)
        self.EntryFun.delete(0, END)


    def __set_value_color(self, button):
        button.config(bg=ask_color())


    @check_scatter_input
    def __collect_scatter(self):
        from Utils.make_data_update_dict import make_data_update_dict
        id = generate_uuid()
        x = self.EntryX.get()
        y = self.EntryY.get()
        marker = "."
        color = self.colorButtonScatter["bg"]
        size = 1
        data = make_data_update_dict(id=id, values=(x, y, marker, color, size), action=CREATE, type=SCATTER)
        return data

    @check_function_input
    def __collect_function(self):
        from Utils.make_data_update_dict import make_data_update_dict
        id = generate_uuid()
        func = self.EntryFun.get()
        line = "-"
        color = self.colorButtonFunc["bg"]
        size = 1
        data = make_data_update_dict(id=id,values=(func,line,color,size),action=CREATE, type=FUNCTION)
        return data