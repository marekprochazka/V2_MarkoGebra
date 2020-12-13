from tkinter import Frame, HORIZONTAL, Scale, OUTSIDE, IntVar
from tkinter import ttk as t

from GUI.settings_components import LimitsSettings, GridSettings
from Globals.calculated import fonts
from Static.constants import NOISE, MAX_WIDTH, MAX_HEIGHT
from Bases import BaseColorPicker

from Globals.variables import Variables as V
from Utils.generate_noise import generate_noise


class Noise(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = NOISE
        self.dispersion_variable = IntVar()
        self.quantity_variable = IntVar()
        self.dispersion_variable.set(1)
        self.quantity_variable.set(1)
        self.live_seed = None

        self.generate_button = t.Button(self, text="Generuj", command=self.__create_live_generation)  # TODO make generation
        self.generate_button.grid(row=0, column=0, sticky="nswe")
        self.lock = t.Button(self, text="Uzamknout",
                             command=lambda: print("todo"))  # TODO lock/save generation
        self.lock.grid(row=0, column=1, sticky="nswe")

        self.quantity_label = t.Label(self, text="Množství", font=fonts()["SMALL_FONT"])
        self.quantity_label.grid(row=1, column=0, sticky="nswe", pady=10)
        self.dispersion_label = t.Label(self, text="Rozptyl", font=fonts()["SMALL_FONT"])
        self.dispersion_label.grid(row=1, column=1, sticky="nswe", pady=10)

        self.quantity = Scale(self, activebackground="aqua", bd=0, from_=1, to=100, orient=HORIZONTAL,
                              variable=self.quantity_variable)
        self.quantity.grid(row=2, column=0, sticky="we")
        self.quantity.bind("<ButtonRelease-1>",
                           lambda event: print(
                               "TODO"))  # TODO UPDATE QUANTITY (add one to existsing generation will be so cool)

        self.dispersion = Scale(self, activebackground="aqua", bd=0, from_=1, to=100, orient=HORIZONTAL,
                                variable=self.dispersion_variable)
        self.dispersion.grid(row=2, column=1, sticky="we")
        self.dispersion.bind("<ButtonRelease-1>", lambda event: print("todo"))  # TODO update dispersion on existing

        self.color = BaseColorPicker(self)
        self.color.grid(row=3, column=0, columnspan=2, sticky="we", pady=10)

        # LIMITS SETTINGS
        self.limits_settings = LimitsSettings(parent=self, controller=controller)
        self.limits_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .001, y=MAX_HEIGHT * .15,
                                   width=MAX_WIDTH * .18,
                                   height=MAX_HEIGHT * .3)

        # GRID SETTINGS
        self.grid_settings = GridSettings(parent=self, controller=controller)
        self.grid_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .25, y=MAX_HEIGHT * .15,
                                 width=MAX_WIDTH * .14,
                                 height=MAX_HEIGHT * .8)

    def __create_live_generation(self):
        live_noise, self.live_seed = generate_noise(self.quantity_variable.get(), self.dispersion_variable.get())
        V.live_noise = [live_noise,"blue","."]
        print(live_noise)
        print(self.live_seed)
