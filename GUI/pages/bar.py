from tkinter import Frame, Label
from tkinter import ttk as t
from Globals.calculated import fonts

class Bar(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = "bar"
        self.basic_colors = ["b", "g", "r", "c", "m", "gold", "k"]
        self.cb_values = ["Modrá", "Zelená", "Červená", "Světle modrá", "Fialová", "Žlutá", "Černá"]

        self.txt1 = t.Label(self, text="Množství:", font=fonts()["SMALL_FONT"])
        self.txt2 = t.Label(self, text="Název:", font=fonts()["SMALL_FONT"])
        self.txt3 = t.Label(self, text="Barva:", font=fonts()["SMALL_FONT"])

        self.value = t.Entry(self, justify="center")
        self.name = t.Entry(self, justify="center")
        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.go = t.Button(self, text="Zapsat hodnotu",
                           command=lambda: controller.add_bar_data(self.name.get(), self.value.get(),
                                                                   self.basic_colors[self.color.current()], self.name,
                                                                   self.value, self.color, self.errorText))

        self.errorText = Label(self, text="", fg="red")
        self.errorText.grid(row=4, column=0)

        self.txt1.grid(row=0, column=0, sticky="we")
        self.txt2.grid(row=1, column=0, sticky="we")
        self.txt3.grid(row=2, column=0, sticky="we")

        self.value.grid(row=0, column=1, sticky="we", padx=20)
        self.name.grid(row=1, column=1, sticky="we", padx=20)
        self.color.grid(row=2, column=1, sticky="we", padx=20)
        self.go.grid(row=3, column=1, sticky="we", padx=20)
