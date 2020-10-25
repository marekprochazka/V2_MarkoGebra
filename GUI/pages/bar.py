from tkinter import Frame, Label
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import BAR, CREATE
from Bases import BaseLabel, BaseEntry
from Static.constants import BASIC_COLORS_NAMES,BASIC_COLORS_VALUES
from Utils.uuid import generate_uuid


# GUI OF BAR INPUTS
class Bar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        from Utils.update_data import update_data

        self.controller = controller
        self.type = BAR
        from Decorators.input_checkers import check_bar_input

        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # PREDEFINED VALUES FOR MULTISELECTS
        # TODO SUBSTITUTE BY COLORWHEELS
        self.basic_colors = BASIC_COLORS_VALUES
        self.cb_values = BASIC_COLORS_NAMES

        # DEFINIG TK OBJECTS
        self.txt1 = BaseLabel(self, text="Množství:")
        self.txt2 = BaseLabel(self, text="Název:")
        self.txt3 = BaseLabel(self, text="Barva:")

        self.value = BaseEntry(self)
        self.name = BaseEntry(self)
        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.go = t.Button(self, text="Zapsat hodnotu",
                           command=lambda: update_data(check_bar_input(self.__collect_data)() ,self.controller.update_list_view))

        # ERROR MESSAGES IF THERE ARE ANY
        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)

        # PLACING TO GRID
        self.txt1.grid(row=0, column=0, sticky="we")
        self.txt2.grid(row=1, column=0, sticky="we")
        self.txt3.grid(row=2, column=0, sticky="we")

        self.value.grid(row=0, column=1, sticky="we", padx=20)
        self.name.grid(row=1, column=1, sticky="we", padx=20)
        self.color.grid(row=2, column=1, sticky="we", padx=20)
        self.go.grid(row=3, column=1, sticky="we", padx=20)

    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict

        id = generate_uuid()
        name = self.name.get()
        value = self.value.get()
        color = self.color.get()
        width = 0.8
        data = make_data_update_dict(id=id, values=(name,value,color,width), action=CREATE)
        return data