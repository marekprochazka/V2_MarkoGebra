from tkinter import Frame,Label
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import MATH
from Bases import BaseEntry,BaseLabel

#GUI OF MATH INPUTS
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

        self.placeButtonScatter = t.Button(self, text="Vložit",
                                           command=lambda: controller.add_point_scatter(self.EntryX.get(),
                                                                                        self.EntryY.get(),
                                                                                        error=self.ErrorWarning,
                                                                                        entry1=self.EntryX,
                                                                                        entry2=self.EntryY))
        self.placeButtonScatter.grid(row=0, column=4, sticky="we")

        # FUNCTION INPUT PART
        self.labelFun = BaseLabel(self, text="f(x):")
        self.labelFun.grid(row=1, column=0)

        self.EntryFun = BaseEntry(self)

        self.EntryFun.grid(row=1, column=1, columnspan=3, sticky="we")

        self.placeButtonPlot = t.Button(self, text="Odložit",
                                        command=lambda: controller.add_plot_from_function(self.EntryFun.get(),
                                                                                          error=self.ErrorWarning,
                                                                                          entry=self.EntryFun))

        self.placeButtonPlot.grid(row=1, column=4, sticky="we", pady=20)

        self.ErrorWarning = Label(self, text="", font=fonts()["SMALL_FONT"], fg="red")
        self.ErrorWarning.grid(row=2, column=2)

        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(3, weight=3)
        self.grid_columnconfigure(4, weight=2)
