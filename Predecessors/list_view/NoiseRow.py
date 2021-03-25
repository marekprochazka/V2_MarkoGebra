from Bases import BaseRow, BaseLabel, BaseColorPicker, BaseEntry
from tkinter import StringVar, Button
from tkinter import ttk as t

from Decorators.input_checkers import noise_input_controller
from Globals.variables import Variables as V

# VALUE [id, seed, dispersion, quantity, color, marker, noise]
# VALUE IS IN FORM AS IT IS SAVED IN CACHE AND IN DATABASE

from Static.constants import POINT_MARKERS, MAX_NOISE_DISPERSION, MAX_NOISE_QUANTITY, CREATE, UPDATE


class NoiseRow(BaseRow):
    def __init__(self, parent, noise_value, controller):
        super().__init__(parent, noise_value, controller)

        # DEFINING VARIABLES
        self.variable_quantity = StringVar()
        self.variable_dispersion = StringVar()
        self.variable_quantity.set(self.value[3])
        self.variable_dispersion.set(self.value[2])

        # TRACERS FOR MAXIMUM VALUES DEFINED IN CONSTANTS
        self.variable_quantity.trace("w", self.__validate_max_quantity_value)
        self.variable_dispersion.trace("w", self.__validate_max_dispersion_value)

        # GUI, *ENTRIES WITH VALIDATE COMMANDS
        self.label_quantity = BaseLabel(self.parent, text="Množství:")
        self.entry_quantity = BaseEntry(self.parent, textvariable=self.variable_quantity, width=8, positive=True)

        self.label_dispersion = BaseLabel(self.parent, text="Rozptyl:")
        self.entry_dispersion = BaseEntry(self.parent, textvariable=self.variable_dispersion, width=8, positive=True)

        self.label_marker = BaseLabel(self.parent, text="Značka:")
        self.combobox_markerType = t.Combobox(self.parent, values=POINT_MARKERS, state="readonly",
                                              width=5)
        self.combobox_markerType.current(POINT_MARKERS.index(self.value[5]))

        self.colorPicker = BaseColorPicker(self.parent, color=self.value[4], width=10)

        self.label_quantity.grid(row=0, column=0)
        self.entry_quantity.grid(row=0, column=1, padx=3)
        self.label_dispersion.grid(row=0, column=2)
        self.entry_dispersion.grid(row=0, column=3, padx=3)
        self.label_marker.grid(row=0, column=4)
        self.combobox_markerType.grid(row=0, column=5, padx=3)
        self.colorPicker.grid(row=0, column=6, padx=3)
        self.button_delete.grid(row=0, column=7, padx=3)
        self.button_save.grid(row=0, column=8, padx=3)

    # VALIDATIONS FOR QUANTITY AND DISPERSION
    def __validate_max_quantity_value(self, *args):
        if len(self.variable_quantity.get()) >= len(str(MAX_NOISE_QUANTITY)):
            if int(self.variable_quantity.get()) > MAX_NOISE_QUANTITY:
                self.variable_quantity.set(MAX_NOISE_QUANTITY)

    def __validate_max_dispersion_value(self, *args):
        if len(self.variable_dispersion.get()) >= len(str(MAX_NOISE_DISPERSION)):
            if int(self.variable_dispersion.get()) > MAX_NOISE_QUANTITY:
                self.variable_dispersion.set(MAX_NOISE_DISPERSION)

    # collect_data FUNCTION IS USED IN BASE AS PARAMETER TO update_data FUNCTION
    @noise_input_controller
    def collect_data(self):
        from Utils.make_data_update_dict import make_data_update_dict
        from Utils.uuid import format_existing_uuid
        from Utils.generate_noise import generate_noise

        id = format_existing_uuid(self.value[0])
        seed = self.value[1]
        dispersion = int(self.variable_dispersion.get()) if self.variable_dispersion.get() else None
        quantity = int(self.variable_quantity.get()) if self.variable_quantity.get() else None
        noise_data, _ = generate_noise(dispersion=dispersion,quantity=quantity,seed=seed) if quantity and dispersion else (None, None)
        color = self.colorPicker["bg"]
        marker = self.combobox_markerType.get()
        data = make_data_update_dict(noise=True, id=id, values=(seed, dispersion, quantity, color, marker),
                                     action=UPDATE, noise_data=noise_data)
        return data
