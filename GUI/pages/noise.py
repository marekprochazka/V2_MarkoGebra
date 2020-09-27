from tkinter import Frame,HORIZONTAL,Scale
from tkinter import ttk as t
from Globals.calculated import fonts
from Static.constants import NOISE

class Noise(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = NOISE
        self.old_type = "noise" #TODO delete after Data update

        self.basic_colors = ["b", "g", "r", "c", "m", "gold", "k"]
        self.cb_values = ["Modrá", "Zelená", "Červená", "Světle modrá", "Fialová", "Žlutá", "Černá"]

        self.number = Scale(self, activebackground="aqua", bd=0, from_=0, to=100, orient=HORIZONTAL)
        self.number.grid(row=0, column=0, sticky="we")
        self.number.bind("<ButtonRelease-1>",
                         lambda event: controller.create_basic_gen(self.number.get(), self.dispersion.get(),
                                                                   self.basic_colors[self.color.current()]))
        self.number_label = t.Label(self, text="Množství", font=fonts()["SMALL_FONT"])
        self.number_label.grid(row=0, column=1, sticky="nswe", padx=15)

        self.dispersion = Scale(self, activebackground="aqua", bd=0, from_=0, to=100, orient=HORIZONTAL)
        self.dispersion.grid(row=1, column=0, sticky="we")
        self.dispersion.bind("<ButtonRelease-1>", lambda event: controller.update_dispersion(self.dispersion.get(),
                                                                                             self.basic_colors[
                                                                                                 self.color.current()]))
        self.dispersion_label = t.Label(self, text="Rozptyl", font=fonts()["SMALL_FONT"])
        self.dispersion_label.grid(row=1, column=1, sticky="S", padx=15)

        self.color = t.Combobox(self, values=self.cb_values, state="readonly")
        self.color.grid(row=2, column=0, sticky="we", pady=10)
        self.color.bind('<<ComboboxSelected>>',
                        lambda event: controller.update_dispersion(self.dispersion.get(),
                                                                   self.basic_colors[self.color.current()]))

        self.lock = t.Button(self, text="Uzamknout",
                             command=lambda: controller.lock_noise(self.dispersion.get(), self.number.get()))
        self.lock.grid(row=3, column=0, sticky="we")
