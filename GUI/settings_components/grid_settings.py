from tkinter import Frame, Scale, HORIZONTAL
from tkinter import ttk as t

from Bases import BaseLabel
from Globals.calculated import fonts

# COMPONENT OF GRID SETTING USED IN MATH AND NOISE
class GridSettings(Frame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.controller = controller

        # GRID SETTINGS

        self.grid_info_label = BaseLabel(self, text="Nastavení mřížky",
                                         font=fonts()["LARGE_FONT"])
        self.grid_info_label.grid(row=0, column=0, pady=15)

        self.Col_button = t.Button(self, text="Změnit barvu",
                                   command=lambda: self.controller.colorize_grid())
        self.Col_button.grid(row=1, column=0, sticky="we", pady=15)

        self.size_label = BaseLabel(self, text="Velikost mřížky")
        self.size_label.grid(row=2, column=0, sticky="we")

        self.grid_size = Scale(self, activebackground="aqua", bd=0, from_=0, to=50,
                               orient=HORIZONTAL, sliderlength=22)
        self.grid_size.set(1)
        self.grid_size.grid(row=3, column=0, sticky="we")
        self.grid_size.bind("<ButtonRelease-1>",
                            lambda event: self.controller.size_grid(self.grid_size.get() / 10))

        self.line_label = BaseLabel(self, text="Druh mřížky")
        self.line_label.grid(row=4, column=0, sticky="we", pady=15)

        self.cbb_convertion = ["-", "--", "-.", ":", ""]
        self.cbb_line = t.Combobox(self, values=["'-'", "'--'", "'-.'", "':'", "' '"],
                                   state="readonly")
        self.cbb_line.current(0)
        self.cbb_line.bind('<<ComboboxSelected>>',
                           lambda event: self.controller.line_grid(self.cbb_convertion[self.cbb_line.current()]))
        self.cbb_line.grid(row=5, column=0, sticky="we")

        self.grid_columnconfigure(0, weight=2)