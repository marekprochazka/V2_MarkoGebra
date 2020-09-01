from tkinter import Frame, Label
from tkinter import ttk as t
from Globals.calculated import fonts

class Pie(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "pie"
        self.basic_colors = ["b", "g", "r", "c", "m", "gold", "k"]
        self.cb_values = ["Modrá", "Zelená", "Červená", "Světle modrá", "Fialová", "Žlutá", "Černá"]

        self.txt1 = t.Label(self, text="Množství:", font=fonts()["SMALL_FONT"])
        self.txt2 = t.Label(self, text="Název:", font=fonts()["SMALL_FONT"])
        self.txt3 = t.Label(self, text="Barva:", font=fonts()["SMALL_FONT"])

        self.slice = t.Entry(self, justify="center")
        self.label = t.Entry(self, justify="center")
        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.add_value = t.Button(self, text="Přidat hodnotu", command=lambda: controller.add_pie_data(
            [self.slice.get(), self.label.get(), self.basic_colors[self.color.current()]], entry1=self.slice,
            entry2=self.label,
            cbb=self.color, error=self.errorText))

        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)
        self.txt1.grid(row=0, column=0, sticky="we")
        self.txt2.grid(row=1, column=0, sticky="we")
        self.txt3.grid(row=2, column=0, sticky="we")

        self.slice.grid(row=0, column=1, sticky="we", padx=20)
        self.label.grid(row=1, column=1, sticky="we", padx=20)
        self.color.grid(row=2, column=1, sticky="we", padx=20)
        self.add_value.grid(row=3, column=1, sticky="we", padx=20)
