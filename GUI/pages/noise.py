from tkinter import Frame, HORIZONTAL, Scale, OUTSIDE, IntVar
from tkinter import ttk as t

from GUI.settings_components import GridSettings
from Globals.calculated import fonts
from Static.constants import NOISE, MAX_WIDTH, MAX_HEIGHT, CREATE, MAX_NOISE_QUANTITY, MAX_NOISE_DISPERSION
from Bases import BaseColorPicker

from Globals.variables import Variables as V
from Utils.ask_color import ask_color
from Utils.generate_noise import generate_noise
from Utils.uuid import generate_uuid

class Noise(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.type = NOISE
        # THIS VARIABLE IS USED IN "new_show_frame.py"
        # AND HAS ONE OF THE VALUES THAT IS CAPABLE
        # FOR GLOBAL VARIABLE "to_animate" WHICH DEFINES
        # WHAT GRAPHING METHOD IS CURRENTLY DRAWING

        # DEFINITIONS
        self.variable_dispersion = IntVar()
        self.variable_quantity = IntVar()
        self.variable_dispersion.set(1)
        self.variable_quantity.set(1)
        self.live_seed = None

        # GUI DEFINITION/GRIDING
        self.button_generateLiveSeed = t.Button(self, text="Generuj",
                                                command=self.__create_live_generation)
        self.button_generateLiveSeed.grid(row=3, column=0, sticky="nswe")
        self.button_lockLiveSeed = t.Button(self, text="Uzamknout",
                                            command=self.__update_noise_data)
        self.button_lockLiveSeed.grid(row=3, column=1, sticky="nswe")

        self.label_quantity = t.Label(self, text="Množství", font=fonts()["SMALL_FONT"])
        self.label_quantity.grid(row=0, column=0, sticky="nswe", pady=10)
        self.label_dispersion = t.Label(self, text="Rozptyl", font=fonts()["SMALL_FONT"])
        self.label_dispersion.grid(row=0, column=1, sticky="nswe", pady=10)

        self.scale_quantity = Scale(self, activebackground="aqua", bd=0, from_=1, to=MAX_NOISE_QUANTITY, orient=HORIZONTAL,
                                    variable=self.variable_quantity)
        self.scale_quantity.grid(row=1, column=0, sticky="we")
        self.scale_quantity.bind("<ButtonRelease-1>",
                                 lambda event: self.__do_live_update())

        self.scale_dispersion = Scale(self, activebackground="aqua", bd=0, from_=1, to=MAX_NOISE_DISPERSION, orient=HORIZONTAL,
                                      variable=self.variable_dispersion)
        self.scale_dispersion.grid(row=1, column=1, sticky="we")
        self.scale_dispersion.bind("<ButtonRelease-1>", lambda event: self.__do_live_update())

        self.colorPicker = BaseColorPicker(self, special_command=self.noise_update_color)
        self.colorPicker.bind("<ButtonRelease-1>", lambda event: self.__do_live_update())
        self.colorPicker.grid(row=2, column=0, columnspan=2, sticky="we", pady=10)

        # LIMITS SETTINGS
        # self.limits_settings = LimitsSettings(parent=self, controller=controller)
        # self.limits_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .001, y=MAX_HEIGHT * .15,
        #                            width=MAX_WIDTH * .18,
        #                            height=MAX_HEIGHT * .3)

        # GRID SETTINGS
        self.grid_settings = GridSettings(parent=self, controller=controller)
        self.grid_settings.place(bordermode=OUTSIDE, x=MAX_WIDTH * .001, y=MAX_HEIGHT * .17,
                                   width=MAX_WIDTH * .18,
                                   height=MAX_HEIGHT * .3)

    # MAKING LIVE NOISE
    def __create_live_generation(self):
        live_noise, self.live_seed = generate_noise(quantity=self.variable_quantity.get(),
                                                    dispersion=self.variable_dispersion.get())
        V.live_noise = [live_noise, self.colorPicker["bg"], "."]

    # UPDATING LIVE NOISE
    def __do_live_update(self):
        if self.live_seed:
            live_noise, self.live_seed = generate_noise(quantity=self.variable_quantity.get(),
                                                        dispersion=self.variable_dispersion.get(),
                                                        seed=self.live_seed)
            V.live_noise = [live_noise, self.colorPicker["bg"], "."]
        else:
            print("pass")

    # COLLECTING DATA AND PACKING THEM TO DICT FORMATTED FOR 'update_data'
    def __collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        id = generate_uuid()
        seed = self.live_seed
        noise_data = V.live_noise[0]
        dispersion = self.variable_dispersion.get()
        quantity = self.variable_quantity.get()
        color = self.colorPicker["bg"]
        marker = V.live_noise[2]
        data = make_data_update_dict(noise=True, id=id,values=(seed,dispersion,quantity,color,marker),action=CREATE, noise_data=noise_data)
        return data

    # EXTENDED UPDATE DATA FUNCTION
    def __update_noise_data(self):
        if self.live_seed:
            from Utils.update_data import update_data
            update_data(data=self.__collect_data(), update_fun=self.controller.update_list_view)
            self.live_seed = None
            self.variable_quantity.set(1)
            self.variable_dispersion.set(1)
            self.scale_quantity.set(1)
            self.scale_dispersion.set(1)

    # SPECIAL COMMAND FOR 'base color picker'
    def noise_update_color(self):
        self.colorPicker.config(bg=ask_color())
        self.__do_live_update()