from tkinter import Frame, Label
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import PIE
from Bases import BaseLabel,BaseEntry

class Pie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = PIE
        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # PREDEFINED VALUES FOR MULTISELECTS
        # TODO SUBSTITUTE BY COLORWHEELS
        self.basic_colors = ["b", "g", "r", "c", "m", "gold", "k"]
        self.cb_values = ["Modrá", "Zelená", "Červená", "Světle modrá", "Fialová", "Žlutá", "Černá"]

        #DEFINIG TK OBJECTS
        self.txt1 = BaseLabel(self, text="Množství:")
        self.txt2 = BaseLabel(self, text="Název:")
        self.txt3 = BaseLabel(self, text="Barva:")

        self.slice = BaseEntry(self)
        self.label = BaseEntry(self)
        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.add_value = t.Button(self, text="Přidat hodnotu", command=lambda: controller.add_pie_data(
            [self.slice.get(), self.label.get(), self.basic_colors[self.color.current()]], entry1=self.slice,
            entry2=self.label,
            cbb=self.color, error=self.errorText))

        #ERROR MESSAGES IF THERE ARE ANY
        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)
        self.txt1.grid(row=0, column=0, sticky="we")
        self.txt2.grid(row=1, column=0, sticky="we")
        self.txt3.grid(row=2, column=0, sticky="we")

        #PLACING TO GRID
        self.slice.grid(row=0, column=1, sticky="we", padx=20)
        self.label.grid(row=1, column=1, sticky="we", padx=20)
        self.color.grid(row=2, column=1, sticky="we", padx=20)
        self.add_value.grid(row=3, column=1, sticky="we", padx=20)
