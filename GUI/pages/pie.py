from tkinter import Frame, Label, END
from tkinter import ttk as t

from Decorators.input_checkers import pie_input_controller
from Static.constants import PIE, CREATE
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
        self.label_slice = BaseLabel(self, text="Množství:")
        self.label_label = BaseLabel(self, text="Název:")
        self.label_color = BaseLabel(self, text="Barva:")

        self.entry_slice = BaseEntry(self, floating=True)
        self.entry_label = BaseEntry(self)
        self.colorPicker = BaseColorPicker(self)

        self.button_enterValue = t.Button(self, text="Přidat hodnotu",
                                          command=lambda: self.__update_data())

        # ERROR MESSAGES IF THERE ARE ANY
        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)
        self.label_slice.grid(row=0, column=0, sticky="we")
        self.label_label.grid(row=1, column=0, sticky="we")
        self.label_color.grid(row=2, column=0, sticky="we")

        # PLACING TO GRID
        self.entry_slice.grid(row=0, column=1, sticky="we", padx=20)
        self.entry_label.grid(row=1, column=1, sticky="we", padx=20)
        self.colorPicker.grid(row=2, column=1, sticky="we", padx=20)
        self.button_enterValue.grid(row=3, column=1, sticky="we", padx=20)

    # EXTENDED UPDATE DATA FUNCTION
    def __update_data(self):
        from Utils.update_data import update_data

        update_data(self.__collect_data(), self.controller.update_list_view)
        self.entry_slice.delete(0, END)
        self.entry_label.delete(0, END)

    # COLLECTING DATA AND PACKING THEM TO DICT FORMATTED FOR 'update_data'
    @pie_input_controller
    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict

        id = generate_uuid()
        slice = float(self.entry_slice.get()) if self.entry_slice.get() else None
        activity = self.entry_label.get()
        color = self.colorPicker["bg"]
        explode = 0.0
        data = make_data_update_dict(id=id, values=(slice, activity, color, explode), action=CREATE)
        return data
