from tkinter import Frame, Label
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import PIE, BASIC_COLORS_VALUES, BASIC_COLORS_NAMES, CREATE
from Bases import BaseLabel, BaseEntry
from Utils.uuid import generate_uuid


class Pie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        from Utils.update_data import update_data
        from Decorators.input_checkers import check_pie_input

        self.controller = controller
        self.type = PIE
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

        self.slice = BaseEntry(self)
        self.label = BaseEntry(self)
        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.add_value = t.Button(self, text="Přidat hodnotu",
                                  command=lambda: update_data(check_pie_input(self.__collect_data)(),
                                                              self.controller.update_list_view))

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

    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict

        id = generate_uuid()
        slice = self.slice.get()
        activity = self.label.get()
        color = self.basic_colors[self.color.current()]
        explode = 0
        data = make_data_update_dict(id=id, values=(slice, activity, color, explode), action=CREATE)
        return data
