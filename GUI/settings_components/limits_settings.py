from tkinter import Frame, CENTER, IntVar, END

from Bases import BaseLabel, BaseEntry
from Globals.calculated import fonts
from Static.constants import X, MIN, MAX, Y
from tkinter import ttk as t
from Globals.variables import Variables as V


class LimitsSettings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # LIMITS SETTINGS
        self.limits_info_label = BaseLabel(self, text="Nastavení limit",
                                           font=fonts()["LARGE_FONT"], anchor=CENTER)
        self.limits_info_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=35, pady=15)

        self.limits_entry_x_min_title = BaseLabel(self, text="min x", anchor=CENTER)
        self.limits_entry_x_min_title.grid(row=1, column=0, sticky="we")
        self.limits_entry_x_max_title = BaseLabel(self, text="max x", anchor=CENTER)
        self.limits_entry_x_max_title.grid(row=1, column=1, sticky="we")
        self.limits_entry_x_min = BaseEntry(self)
        self.limits_entry_x_min.grid(row=2, column=0, sticky="we")
        self.limits_entry_x_max = BaseEntry(self)
        self.limits_entry_x_max.grid(row=2, column=1, sticky="we", padx=15, pady=15)

        self.limits_entry_y_min_title = BaseLabel(self, text="min y", anchor=CENTER)
        self.limits_entry_y_min_title.grid(row=3, column=0, sticky="we")
        self.limits_entry_y_max_title = BaseLabel(self, text="max y", anchor=CENTER)
        self.limits_entry_y_max_title.grid(row=3, column=1, sticky="we")
        self.limits_entry_y_min = BaseEntry(self)
        self.limits_entry_y_min.grid(row=4, column=0, sticky="we", pady=15)
        self.limits_entry_y_max = BaseEntry(self)
        self.limits_entry_y_max.grid(row=4, column=1, sticky="we", padx=15, pady=15)

        # TAKES ENTRY VALUES AND EXECUTES UPDATE FUNCTION
        self.limits_execute_update_button = t.Button(self, text="Aktualizovat limity",
                                                     command=lambda: self.__update_limits())
        self.limits_execute_update_button.grid(row=5, column=0, columnspan=2, sticky="we")

        self.limits_auto_update_checkbox_title = BaseLabel(self, text="Autoupdate")
        # IS AUTO UPDATE ALLOWED CHECKBOX
        self.limits_auto_update_checkbox_check_var = IntVar(value=1)
        self.limits_auto_update_checkbox_title.grid(row=6, column=0, sticky="we")
        self.limits_auto_update_checkbox = t.Checkbutton(self,
                                                         variable=self.limits_auto_update_checkbox_check_var,
                                                         command=lambda: self.controller.__switch_auto_limit_update_value())
        self.limits_auto_update_checkbox.grid(row=6, column=1, sticky="we")

        # UPDATE FE VALUES BY BE VALUES
        self.__init_limits_entries_by_global_variables()

    def __init_limits_entries_by_global_variables(self):
        for e in (
                self.limits_entry_x_min, self.limits_entry_x_max, self.limits_entry_y_min, self.limits_entry_y_max):
            e.delete(0, END)

        self.limits_entry_x_min.insert(0, V.limits[X][MIN])
        self.limits_entry_x_max.insert(0, V.limits[X][MAX])
        self.limits_entry_y_min.insert(0, V.limits[Y][MIN])
        self.limits_entry_y_max.insert(0, V.limits[Y][MAX])

    def __update_limits(self):
        self.controller.update_limits(self.limits_entry_x_min.get(), self.limits_entry_x_max.get(),
                                      self.limits_entry_y_min.get(), self.limits_entry_y_max.get())
