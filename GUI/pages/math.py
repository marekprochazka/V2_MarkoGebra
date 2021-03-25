from tkinter import Frame, Label, END, OUTSIDE
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import MATH,SCATTER, CREATE, FUNCTION, MAX_WIDTH, MAX_HEIGHT
from Bases import BaseEntry, BaseLabel, BaseColorPicker

from Utils.uuid import generate_uuid
from Decorators.input_checkers import check_function_input, scatter_input_controller
from GUI.settings_components import LimitsSettings, GridSettings


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
        self.label_x = BaseLabel(self, text="X:")
        self.label_y = BaseLabel(self, text="Y:")

        self.label_x.grid(row=0, column=0)
        self.label_y.grid(row=0, column=2)

        self.entry_x = BaseEntry(self, numbers=True)
        self.entry_y = BaseEntry(self, numbers=True)

        self.entry_x.grid(row=0, column=1, sticky="we")
        self.entry_y.grid(row=0, column=3, sticky="we")

        self.colorPicker_scatter = BaseColorPicker(self, width=15)
        self.colorPicker_scatter.grid(row=0, column=4, sticky="we", padx=2)

        self.button_enterValueScatter = t.Button(self, text="Vložit",
                                                 command=lambda: self.__update_data_scatter())
        self.button_enterValueScatter.grid(row=0, column=5, sticky="we")

        # FUNCTION INPUT PART
        self.label_function = BaseLabel(self, text="f(x):")
        self.label_function.grid(row=1, column=0)

        self.entry_function = BaseEntry(self, function=True)

        self.entry_function.grid(row=1, column=1, columnspan=3, sticky="we")

        self.colorPicker_function = BaseColorPicker(self, width=15)
        self.colorPicker_function.grid(row=1, column=4, sticky="we", padx=2)

        self.button_enterValueFunction = t.Button(self, text="Odložit",
                                                  command=lambda: self.__update_data_function())

        self.button_enterValueFunction.grid(row=1, column=5, sticky="we", pady=20)

        self.ErrorWarning = Label(self, text="", font=fonts()["SMALL_FONT"], fg="red")
        self.ErrorWarning.grid(row=2, column=2)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(5, weight=2)

        # LIMITS SETTINGS
        self.limits_settings = LimitsSettings(parent=self, controller=controller)
        self.limits_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .001, y=MAX_HEIGHT * .1,
                                   width=MAX_WIDTH * .18,
                                   height=MAX_HEIGHT * .3)

        # GRID SETTINGS
        self.grid_settings = GridSettings(parent=self, controller=controller)
        self.grid_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .25, y=MAX_HEIGHT * .1,
                                 width=MAX_WIDTH * .14,
                                 height=MAX_HEIGHT * .8)

    # EXTENDED UPDATE FUNCTIONS FOR SCATTER AND FUNCTION INPUTS
    def __update_data_scatter(self):
        from Utils.update_data import update_data
        update_data(self.__collect_scatter(), update_fun=self.controller.update_list_view,
                    limits_fun=self.controller.auto_update_limits_by_scatter_input)
        self.entry_x.delete(0, END)
        self.entry_y.delete(0, END)

    def __update_data_function(self):
        from Utils.update_data import update_data
        update_data(self.__collect_function(), self.controller.update_list_view)
        self.entry_function.delete(0, END)

    # COLLECTING FUNCTIONS, FORMATTING TO 'update_data' FRIENDLY DICT
    @scatter_input_controller
    def __collect_scatter(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.handle_only_minus_input import handle_only_minus_input
        id = generate_uuid()
        x = int(handle_only_minus_input(self.entry_x.get())) if self.entry_x.get() else None
        y = int(handle_only_minus_input(self.entry_y.get())) if self.entry_y.get() else None
        marker = "."
        color = self.colorPicker_scatter["bg"]
        size = 1
        data = make_data_update_dict(id=id, values=(x, y, marker, color, size), action=CREATE, type=SCATTER)
        return data

    @check_function_input
    def __collect_function(self):
        from Utils.make_data_update_dict import make_data_update_dict
        id = generate_uuid()
        func = self.entry_function.get()
        line = "-"
        color = self.colorPicker_function["bg"]
        size = 1
        data = make_data_update_dict(id=id, values=(func, line, color, size), action=CREATE, type=FUNCTION)
        return data
