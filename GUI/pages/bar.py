from tkinter import Frame, Label, END
from tkinter import ttk as t

from Decorators.input_checkers import bar_input_controller
from Globals.calculated import fonts
from Static.constants import BAR, CREATE
from Bases import BaseLabel, BaseEntry, BaseColorPicker
from Static.constants import BASIC_COLORS_NAMES, BASIC_COLORS_VALUES
from Utils.uuid import generate_uuid


# GUI OF BAR INPUTS
class Bar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.type = BAR

        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # DEFINIG TK OBJECTS
        self.label_value = BaseLabel(self, text="Množství:")
        self.label_name = BaseLabel(self, text="Název:")
        self.label_color = BaseLabel(self, text="Barva:")

        self.entry_value = BaseEntry(self, positive=True)
        self.entry_name = BaseEntry(self)
        self.colorPicker = BaseColorPicker(self)
        self.button_enterValue = t.Button(self, text="Zapsat hodnotu",
                                          command=self.__update_data)

        # ERROR MESSAGES IF THERE ARE ANY
        self.label_errorText = Label(self, text="", fg="red")
        self.label_errorText.grid(row=4, column=0)

        # PLACING TO GRID
        self.label_value.grid(row=0, column=0, sticky="we")
        self.label_name.grid(row=1, column=0, sticky="we")
        self.label_color.grid(row=2, column=0, sticky="we")

        self.entry_value.grid(row=0, column=1, sticky="we", padx=20)
        self.entry_name.grid(row=1, column=1, sticky="we", padx=20)
        self.colorPicker.grid(row=2, column=1, sticky="we", padx=20)
        self.button_enterValue.grid(row=3, column=1, sticky="we", padx=20)

    # EXTENDED UPDATE DATA FUNCTION
    def __update_data(self):
        from Utils.update_data import update_data
        update_data(self.__collect_data(), self.controller.update_list_view)
        self.entry_name.delete(0, END)
        self.entry_value.delete(0, END)

    # COLLECTING DATA AND PACKING THEM TO DICT FORMATTED FOR 'update_data'
    @bar_input_controller
    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict

        id = generate_uuid()
        name = self.entry_name.get()
        value = int(self.entry_value.get()) if self.entry_value.get() else None
        color = self.colorPicker["bg"]
        width = 0.8
        data = make_data_update_dict(id=id, values=(name, value, color, width), action=CREATE)
        return data
