from tkinter import Frame, CENTER, IntVar, END

from Bases import BaseLabel, BaseEntry
from Globals.calculated import fonts
from Static.constants import X, MIN, MAX, Y
from tkinter import ttk as t
from Globals.variables import Variables as V

# COMPONENT OF LIMITS SETTINGS USED IN NOISE AND MATH
class LimitsSettings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # LIMITS SETTINGS
        self.label_limitsInfo = BaseLabel(self, text="Nastavení limit",
                                          font=fonts()["LARGE_FONT"], anchor=CENTER)
        self.label_limitsInfo.grid(row=0, column=0, columnspan=2, sticky="we", padx=35, pady=15)

        self.label_minXLimit = BaseLabel(self, text="min x", anchor=CENTER)
        self.label_minXLimit.grid(row=1, column=0, sticky="we")
        self.label_maxXLimit = BaseLabel(self, text="max x", anchor=CENTER)
        self.label_maxXLimit.grid(row=1, column=1, sticky="we")
        self.entry_minXLimit = BaseEntry(self, numbers=True)
        self.entry_minXLimit.grid(row=2, column=0, sticky="we")
        self.entry_maxXLimit = BaseEntry(self, numbers=True)
        self.entry_maxXLimit.grid(row=2, column=1, sticky="we", padx=15, pady=15)

        self.label_minYLimit = BaseLabel(self, text="min y", anchor=CENTER)
        self.label_minYLimit.grid(row=3, column=0, sticky="we")
        self.label_maxYLabel = BaseLabel(self, text="max y", anchor=CENTER)
        self.label_maxYLabel.grid(row=3, column=1, sticky="we")
        self.entry_minYLimit = BaseEntry(self, numbers=True)
        self.entry_minYLimit.grid(row=4, column=0, sticky="we", pady=15)
        self.entry_maxYLimit = BaseEntry(self, numbers=True)
        self.entry_maxYLimit.grid(row=4, column=1, sticky="we", padx=15, pady=15)

        # TAKES ENTRY VALUES AND EXECUTES UPDATE FUNCTION
        self.button_updateLimits = t.Button(self, text="Aktualizovat limity",
                                            command=lambda: self.__update_limits())
        self.button_updateLimits.grid(row=5, column=0, columnspan=2, sticky="we")

        self.label_limitAutoUpdate = BaseLabel(self, text="Autoupdate")
        # IS AUTO UPDATE ALLOWED CHECKBOX
        self.controller.variable_isAutoUpdate = IntVar(value=1)
        self.label_limitAutoUpdate.grid(row=6, column=0, sticky="we")
        self.limits_auto_update_checkbox = t.Checkbutton(self,
                                                         variable=self.controller.variable_isAutoUpdate,
                                                         command=lambda: self.controller.switch_auto_limit_update_value())
        self.limits_auto_update_checkbox.grid(row=6, column=1, sticky="we")

        # UPDATE FE VALUES BY BE VALUES
        self.__init_limits_entries_by_global_variables()

    def __init_limits_entries_by_global_variables(self):
        for e in (
                self.entry_minXLimit, self.entry_maxXLimit, self.entry_minYLimit, self.entry_maxYLimit):
            e.delete(0, END)

        self.entry_minXLimit.insert(0, V.limits[X][MIN])
        self.entry_maxXLimit.insert(0, V.limits[X][MAX])
        self.entry_minYLimit.insert(0, V.limits[Y][MIN])
        self.entry_maxYLimit.insert(0, V.limits[Y][MAX])

    def __update_limits(self):
        self.controller.update_limits(self.entry_minXLimit.get(), self.entry_maxXLimit.get(),
                                      self.entry_minYLimit.get(), self.entry_maxYLimit.get())
