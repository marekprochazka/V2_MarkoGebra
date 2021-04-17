from tkinter import Frame, Scale, HORIZONTAL
from tkinter import ttk as t

from Bases import BaseLabel
from Globals.calculated import fonts


# COMPONENT OF GRID SETTING USED IN MATH AND NOISE
class GridSettings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # GRID SETTINGS

        self.label_gridInfo = BaseLabel(self, text="Nastavení mřížky",
                                        font=fonts()["LARGE_FONT"])
        self.label_gridInfo.grid(row=0, column=0, pady=15)

        self.button_changeGridColor = t.Button(self, text="Změnit barvu",
                                               command=lambda: self.controller.colorize_grid())
        self.button_changeGridColor.grid(row=1, column=0, sticky="we", pady=15)

        self.label_size = BaseLabel(self, text="Velikost mřížky")
        self.label_size.grid(row=2, column=0, sticky="we")

        self.scale_gridSize = Scale(self, activebackground="aqua", bd=0, from_=0, to=50,
                                    orient=HORIZONTAL, sliderlength=22)
        self.scale_gridSize.set(1)
        self.scale_gridSize.grid(row=3, column=0, sticky="we")
        self.scale_gridSize.bind("<ButtonRelease-1>",
                                 lambda event: self.controller.size_grid(self.scale_gridSize.get() / 10))

        self.label_lineType = BaseLabel(self, text="Druh mřížky")
        self.label_lineType.grid(row=4, column=0, sticky="we", pady=15)

        self.conversion_from_combobox = ["-", "--", "-.", ":", ""]
        self.combobox_lineType = t.Combobox(self, values=["'-'", "'--'", "'-.'", "':'", "' '"],
                                            state="readonly")
        self.combobox_lineType.current(0)
        self.combobox_lineType.bind('<<ComboboxSelected>>',
                                    lambda event: self.controller.line_grid(
                                        self.conversion_from_combobox[self.combobox_lineType.current()]))
        self.combobox_lineType.grid(row=5, column=0, sticky="we")

        self.grid_columnconfigure(0, weight=2)
