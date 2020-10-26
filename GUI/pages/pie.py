from tkinter import Frame, Label, END
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import PIE, BASIC_COLORS_VALUES, BASIC_COLORS_NAMES, CREATE
from Bases import BaseLabel, BaseEntry, BaseColorPicker
from Utils.uuid import generate_uuid


class Pie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.type = PIE
        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # DEFINIG TK OBJECTS
        self.txt1 = BaseLabel(self, text="Množství:")
        self.txt2 = BaseLabel(self, text="Název:")
        self.txt3 = BaseLabel(self, text="Barva:")

        self.slice = BaseEntry(self)
        self.label = BaseEntry(self)
        self.color = BaseColorPicker(self)

        self.add_value = t.Button(self, text="Přidat hodnotu",
                                  command=lambda: self.__update_data())

        # ERROR MESSAGES IF THERE ARE ANY
        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)
        self.txt1.grid(row=0, column=0, sticky="we")
        self.txt2.grid(row=1, column=0, sticky="we")
        self.txt3.grid(row=2, column=0, sticky="we")

        # PLACING TO GRID
        self.slice.grid(row=0, column=1, sticky="we", padx=20)
        self.label.grid(row=1, column=1, sticky="we", padx=20)
        self.color.grid(row=2, column=1, sticky="we", padx=20)
        self.add_value.grid(row=3, column=1, sticky="we", padx=20)

    def __update_data(self):
        from Utils.update_data import update_data
        from Decorators.input_checkers import check_pie_input
        update_data(check_pie_input(self.__collect_data)(), self.controller.update_list_view)
        self.slice.delete(0, END)
        self.label.delete(0, END)

    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict

        id = generate_uuid()
        slice = self.slice.get()
        activity = self.label.get()
        color = self.color["bg"]
        explode = 0
        data = make_data_update_dict(id=id, values=(slice, activity, color, explode), action=CREATE)
        return data
