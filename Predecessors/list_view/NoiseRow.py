from Bases import BaseRow, BaseLabel, BaseColorPicker, BaseEntry
from tkinter import StringVar, Button
from tkinter import ttk as t
from Globals.variables import Variables as V

# VALUE [id, seed, dispersion, quantity, color, marker, noise]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE

from Static.constants import POINT_MARKERS, MAX_NOISE_DISPERSION, MAX_NOISE_QUANTITY, CREATE, UPDATE


class NoiseRow(BaseRow):
    def __init__(self, parent, noise_value, controller):
        super().__init__(parent, noise_value, controller)

        # DEFINING VARIABLES
        self.quantity_value = StringVar()
        self.dispersion_value = StringVar()
        self.quantity_value.set(self.value[3])
        self.dispersion_value.set(self.value[2])

        # TRACERS FOR MAXIMUM VALUES DEFINED IN CONSTANTS
        self.quantity_value.trace("w", self.__validate_max_quantity_value)
        self.dispersion_value.trace("w", self.__validate_max_dispersion_value)

        # GUI, *ENTRIES WITH VALIDATE COMMANDS
        self.quantity_label = BaseLabel(self.parent, text="Množství")
        self.quantity_entry = BaseEntry(self.parent, textvariable=self.quantity_value, width=4, numbers=True)

        self.dispersion_label = BaseLabel(self.parent, text="Rozptyl")
        self.dispersion_entry = BaseEntry(self.parent, textvariable=self.dispersion_value, width=4, numbers=True)

        self.marker_label = BaseLabel(self.parent, text="Značka")
        self.marker_multiselect = t.Combobox(self.parent, values=POINT_MARKERS, state="readonly",
                                             width=5)
        self.marker_multiselect.current(POINT_MARKERS.index(self.value[5]))

        self.col_but = BaseColorPicker(self.parent, color=self.value[4], width=10)

        self.quantity_label.grid(row=0, column=0)
        self.quantity_entry.grid(row=0, column=1)
        self.dispersion_label.grid(row=0, column=2)
        self.dispersion_entry.grid(row=0, column=3)
        self.marker_label.grid(row=0, column=4)
        self.marker_multiselect.grid(row=0, column=5)
        self.col_but.grid(row=0, column=6)
        self.del_but.grid(row=0, column=7)
        self.save_but.grid(row=0, column=8)

    # VALIDATIONS FOR QUANTITY AND DISPERSION
    def __validate_max_quantity_value(self, *args):
        if len(self.quantity_value.get()) >= len(str(MAX_NOISE_QUANTITY)):
            if int(self.quantity_value.get()) > MAX_NOISE_QUANTITY:
                self.quantity_value.set(MAX_NOISE_QUANTITY)

    def __validate_max_dispersion_value(self, *args):
        if len(self.dispersion_value.get()) >= len(str(MAX_NOISE_DISPERSION)):
            if int(self.dispersion_value.get()) > MAX_NOISE_QUANTITY:
                self.dispersion_value.set(MAX_NOISE_DISPERSION)

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        from Utils.generate_noise import generate_noise

        id = format_existing_uuid(self.value[0])
        seed = self.value[1]
        dispersion = int(self.dispersion_value.get()) if self.dispersion_value.get() != "" else 1
        quantity = int(self.quantity_value.get()) if self.quantity_value.get() != "" else 1
        noise_data, _ = generate_noise(dispersion=dispersion,quantity=quantity,seed=seed)
        color = self.col_but["bg"]
        marker = self.marker_multiselect.get()
        data = make_data_update_dict(noise=True, id=id, values=(seed, dispersion, quantity, color, marker),
                                     action=UPDATE, noise_data=noise_data)
        return data
