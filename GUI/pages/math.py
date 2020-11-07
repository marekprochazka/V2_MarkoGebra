from tkinter import Frame, Label, Button, END, OUTSIDE, CENTER, IntVar, Scale, HORIZONTAL
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import MATH, CACHE, CHANGES_CACHE, TYPE, SCATTER, DATA, ID, CREATE, FUNCTION, MAX_WIDTH, \
    MAX_HEIGHT, X, MIN, MAX, Y
from Bases import BaseEntry, BaseLabel, BaseColorPicker
from Utils.ask_color import ask_color
from Utils.uuid import generate_uuid
from Decorators.input_checkers import check_function_input, check_scatter_input
from Globals.variables import Variables as V
from GUI.settings_components.limits_settings import LimitsSettings

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

        self.colorButtonScatter = BaseColorPicker(self, width=15)
        self.colorButtonScatter.grid(row=0, column=4, sticky="we", padx=2)

        self.placeButtonScatter = t.Button(self, text="Vložit",
                                           command=lambda: self.__update_data_scatter())
        self.placeButtonScatter.grid(row=0, column=5, sticky="we")

        # FUNCTION INPUT PART
        self.labelFun = BaseLabel(self, text="f(x):")
        self.labelFun.grid(row=1, column=0)

        self.EntryFun = BaseEntry(self)

        self.EntryFun.grid(row=1, column=1, columnspan=3, sticky="we")

        self.colorButtonFunc = BaseColorPicker(self, width=15)
        self.colorButtonFunc.grid(row=1, column=4, sticky="we", padx=2)

        self.placeButtonPlot = t.Button(self, text="Odložit",
                                        command=lambda: self.__update_data_function())

        self.placeButtonPlot.grid(row=1, column=5, sticky="we", pady=20)

        self.ErrorWarning = Label(self, text="", font=fonts()["SMALL_FONT"], fg="red")
        self.ErrorWarning.grid(row=2, column=2)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(5, weight=2)

        # # LIMITS SETTINGS
        self.limits_settings = LimitsSettings(parent=self,controller=controller)
        self.limits_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH*.001, y=MAX_HEIGHT * .1,
                                             width=MAX_WIDTH * .18,
                                             height=MAX_HEIGHT * .3)
    


        # GRID SETTINGS
        self.grid_settings_container = Frame(self)
        self.grid_settings_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .25, y=MAX_HEIGHT * .1,
                                           width=MAX_WIDTH * .14,
                                           height=MAX_HEIGHT * .8)

        self.grid_info_label = BaseLabel(self.grid_settings_container, text="Nastavení mřížky",
                                         font=fonts()["LARGE_FONT"])
        self.grid_info_label.grid(row=0, column=0, pady=15)

        self.Col_button = t.Button(self.grid_settings_container, text="Změnit barvu",
                                   command=lambda: self.controller.colorize_grid())
        self.Col_button.grid(row=1, column=0, sticky="we", pady=15)

        self.size_label = BaseLabel(self.grid_settings_container, text="Velikost mřížky")
        self.size_label.grid(row=2, column=0, sticky="we")

        self.grid_size = Scale(self.grid_settings_container, activebackground="aqua", bd=0, from_=0, to=50,
                               orient=HORIZONTAL, sliderlength=22)
        self.grid_size.set(1)
        self.grid_size.grid(row=3, column=0, sticky="we")
        self.grid_size.bind("<ButtonRelease-1>",
                            lambda event: self.controller.size_grid(self.grid_size.get() / 10))

        self.line_label = BaseLabel(self.grid_settings_container, text="Druh mřížky")
        self.line_label.grid(row=4, column=0, sticky="we", pady=15)

        self.cbb_convertion = ["-", "--", "-.", ":", ""]
        self.cbb_line = t.Combobox(self.grid_settings_container, values=["'-'", "'--'", "'-.'", "':'", "' '"],
                                   state="readonly")
        self.cbb_line.current(0)
        self.cbb_line.bind('<<ComboboxSelected>>',
                           lambda event: self.controller.line_grid(self.cbb_convertion[self.cbb_line.current()]))
        self.cbb_line.grid(row=5, column=0, sticky="we")

        self.grid_settings_container.grid_columnconfigure(0, weight=2)




    def __update_data_scatter(self):
        from Utils.update_data import update_data
        update_data(self.__collect_scatter(), update_fun=self.controller.update_list_view,
                    limits_fun=self.controller.auto_update_limits_by_scatter_input)
        self.EntryX.delete(0, END)
        self.EntryY.delete(0, END)

    def __update_data_function(self):
        from Utils.update_data import update_data
        update_data(self.__collect_function(), self.controller.update_list_view)
        self.EntryFun.delete(0, END)

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
        data = make_data_update_dict(id=id, values=(func, line, color, size), action=CREATE, type=FUNCTION)
        return data

