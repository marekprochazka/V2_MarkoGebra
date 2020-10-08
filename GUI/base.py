from tkinter import Tk, OUTSIDE, Frame, Scale, HORIZONTAL, Canvas, CENTER, END, IntVar
from tkinter import ttk as t

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graphing.setup import f
from Static.constants import MAX_HEIGHT, MAX_WIDTH, MIN, MAX, X, Y
from .pages import Mathematical, Pie, Bar, Noise

from Globals.calculated import fonts

from Globals.variables import Variables as V


# ALL GUI WORK IS SOMEHOW CONNECTED TO THIS (EXCEPTION: "new_show_frame.py")
# FRAMES TO DIFFERENT GRAPHING METHODS ARE CONNECTED TO THIS CLASS
# FRAME CHANGING LOGIC IS MANAGED IN "Utils/new_show_frame.py"
class Base(Tk):
    def __init__(self, main):
        # INITIAL GUI SETUP
        Tk.__init__(self)
        Tk.wm_title(self, "MarkoGebra")
        Tk.minsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        Tk.maxsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        self.main = main

        # TUPLE OF ALL GRAPHING METHODS THAT IS REPRESENTED IN FE BY MULTISESECT
        # TODO ADD NOISE AFTER FINISHING FEATURE
        self.input_frames = (Mathematical, Pie, Bar)
        # self.input_frames = (Mathematical, Pie, Bar, Noise)

        # RELATIVE CONTAINER TO WHICH IS WRITTEN PARTICULAR GRAPHING METHOD
        self.SetupContainer = t.Frame(self, width=MAX_WIDTH * .4, height=MAX_HEIGHT)

        self.SetupContainer.pack(side="top", fill="both", expand=True)

        self.SetupContainer.grid_rowconfigure(0, weight=1)
        self.SetupContainer.grid_columnconfigure(0, weight=1)

        # MATLOPLIB GRAPH REPESENTATION ON FE
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 470, y=MAX_HEIGHT - 470)

        # MULTISELECT OF GRAPHING METHODS
        # AFTER SELECTION THE "show_Setup_Frame" FUNCTION FROM "new_show_frame.py" IS CALLED TO MANAGE FRAME CHANGE
        self.CBB2 = t.Combobox(self, values=["Matematické", "Koláč", "Sloupcový", "Náhodný šum"],
                               state="readonly")
        self.CBB2.bind('<<ComboboxSelected>>',
                       lambda event: self.show_Setup_Frame(self.input_frames[self.CBB2.current()]))
        self.CBB2.current(0)
        self.CBB2.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                        x=MAX_WIDTH * .01, y=MAX_HEIGHT * .05)

        # TOPRIGHT BUTTONS
        self.hint = t.Button(self, command=lambda: self.openHelp(), text="Nápověda")
        self.hint.place(bordermode=OUTSIDE, x=MAX_WIDTH * .94, width=MAX_WIDTH * .06, y=0, height=MAX_HEIGHT * .04)
        self.save_but = t.Button(self, text="uložit jako orázek", command=lambda: self.saver())
        self.save_but.place(bordermode=OUTSIDE, x=MAX_WIDTH * .84, width=MAX_WIDTH * .1, y=0, height=MAX_HEIGHT * .04)
        self.deleteAll_button = t.Button(self, text="Smazat vše", command=lambda: self.delete_all())
        self.deleteAll_button.place(bordermode=OUTSIDE, x=MAX_WIDTH * .74, width=MAX_WIDTH * .1, y=0,
                                    height=MAX_HEIGHT * .04)

        # LIMITS SETTINGS
        self.limits_settings_container = Frame(self)
        self.limits_settings_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .51, y=MAX_HEIGHT * .32,
                                             width=MAX_WIDTH * .18,
                                             height=MAX_HEIGHT * .3)

        self.limits_info_label = t.Label(self.limits_settings_container, text="Nastavení limit",
                                         font=fonts()["LARGE_FONT"], anchor=CENTER)
        self.limits_info_label.grid(row=0, column=0, columnspan=2, sticky="we", padx=35, pady=15)

        self.limits_entry_x_min_title = t.Label(self.limits_settings_container, text="min x",
                                                font=fonts()["SMALL_FONT"], anchor=CENTER)
        self.limits_entry_x_min_title.grid(row=1, column=0, sticky="we")
        self.limits_entry_x_max_title = t.Label(self.limits_settings_container, text="max x",
                                                font=fonts()["SMALL_FONT"], anchor=CENTER)
        self.limits_entry_x_max_title.grid(row=1, column=1, sticky="we")
        self.limits_entry_x_min = t.Entry(self.limits_settings_container, justify="center")
        self.limits_entry_x_min.grid(row=2, column=0, sticky="we")
        self.limits_entry_x_max = t.Entry(self.limits_settings_container, justify="center")
        self.limits_entry_x_max.grid(row=2, column=1, sticky="we", padx=15, pady=15)

        self.limits_entry_y_min_title = t.Label(self.limits_settings_container, text="min y",
                                                font=fonts()["SMALL_FONT"], anchor=CENTER)
        self.limits_entry_y_min_title.grid(row=3, column=0, sticky="we")
        self.limits_entry_y_max_title = t.Label(self.limits_settings_container, text="max y",
                                                font=fonts()["SMALL_FONT"], anchor=CENTER)
        self.limits_entry_y_max_title.grid(row=3, column=1, sticky="we")
        self.limits_entry_y_min = t.Entry(self.limits_settings_container, justify="center")
        self.limits_entry_y_min.grid(row=4, column=0, sticky="we", pady=15)
        self.limits_entry_y_max = t.Entry(self.limits_settings_container, justify="center")
        self.limits_entry_y_max.grid(row=4, column=1, sticky="we", padx=15, pady=15)

        # TAKES ENTRY VALUES AND EXECUTES UPDATE FUNCTION
        self.limits_execute_update_button = t.Button(self.limits_settings_container, text="Aktualizovat limity",
                                                     command=lambda: self.__update_limits())
        self.limits_execute_update_button.grid(row=5, column=0, columnspan=2, sticky="we")

        self.limits_auto_update_checkbox_title = t.Label(self.limits_settings_container, text="Autoupdate",
                                                         font=fonts()["SMALL_FONT"])
        self.limits_auto_update_checkbox_check_var = IntVar(value=1)
        self.limits_auto_update_checkbox_title.grid(row=6, column=0, sticky="we")
        self.limits_auto_update_checkbox = t.Checkbutton(self.limits_settings_container,
                                                         variable=self.limits_auto_update_checkbox_check_var,
                                                         command=lambda: self.__switch_auto_limit_update_value())
        self.limits_auto_update_checkbox.grid(row=6, column=1, sticky="we")

        # UPDATE FE VALUES BY BE VALUES
        self.set_limits_entries_values_by_global_variables()

        # GRID SETTINGS
        self.grid_settings_container = Frame(self)
        self.grid_settings_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .55, y=MAX_HEIGHT * .67,
                                           width=MAX_WIDTH * .14,
                                           height=MAX_HEIGHT * .8)

        self.grid_info_label = t.Label(self.grid_settings_container, text="Nastavení mřížky",
                                       font=fonts()["LARGE_FONT"])
        self.grid_info_label.grid(row=0, column=0, pady=15)

        self.Col_button = t.Button(self.grid_settings_container, text="Změnit barvu",
                                   command=lambda: self.colorize_grid())
        self.Col_button.grid(row=1, column=0, sticky="we", pady=15)

        self.size_label = t.Label(self.grid_settings_container, text="Velikost mřížky")
        self.size_label.grid(row=2, column=0, sticky="we")

        self.grid_size = Scale(self.grid_settings_container, activebackground="aqua", bd=0, from_=0, to=50,
                               orient=HORIZONTAL, sliderlength=22)
        self.grid_size.set(1)
        self.grid_size.grid(row=3, column=0, sticky="we")
        self.grid_size.bind("<ButtonRelease-1>",
                            lambda event: self.size_grid(self.grid_size.get() / 10))

        self.line_label = t.Label(self.grid_settings_container, text="Druh mřížky")
        self.line_label.grid(row=4, column=0, sticky="we", pady=15)

        self.cbb_convertion = ["-", "--", "-.", ":", ""]
        self.cbb_line = t.Combobox(self.grid_settings_container, values=["'-'", "'--'", "'-.'", "':'", "' '"],
                                   state="readonly")
        self.cbb_line.current(0)
        self.cbb_line.bind('<<ComboboxSelected>>',
                           lambda event: self.line_grid(self.cbb_convertion[self.cbb_line.current()]))
        self.cbb_line.grid(row=5, column=0, sticky="we")

        self.grid_settings_container.grid_columnconfigure(0, weight=2)

        # GRAPHING INPUTS LIST
        self.Table_container = t.Frame(self)
        self.canvas = Canvas(self.Table_container)
        self.scrollbar = t.Scrollbar(self.Table_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = t.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.update_table()
        for i in range(50):
            Frame(self.scrollable_frame).pack()

        self.Table_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .6, width=MAX_WIDTH * .4,
                                   height=MAX_HEIGHT * .3)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # OPEN CONSOLE BUTTON
        self.console = t.Button(self, text="Konzole", command=lambda: self.console_controller())
        self.console.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .95, height=MAX_HEIGHT * .05,
                           width=MAX_WIDTH * .4)

        # RELATIVE FRAMES

        self.SetupFrames = {}

        self._frame = None
        self.show_Setup_Frame(cont=Mathematical)

    def set_limits_entries_values_by_global_variables(self):
        for e in (self.limits_entry_x_min, self.limits_entry_x_max, self.limits_entry_y_min, self.limits_entry_y_max):
            e.delete(0, END)

        self.limits_entry_x_min.insert(0, V.limits[X][MIN])
        self.limits_entry_x_max.insert(0, V.limits[X][MAX])
        self.limits_entry_y_min.insert(0, V.limits[Y][MIN])
        self.limits_entry_y_max.insert(0, V.limits[Y][MAX])

    def __update_limits(self):
        self.main.update_limits(int(self.limits_entry_x_min.get()), int(self.limits_entry_x_max.get()),
                                int(self.limits_entry_y_min.get()), int(self.limits_entry_y_max.get()))

    def __switch_auto_limit_update_value(self):
        V.is_auto_update = self.limits_auto_update_checkbox_check_var.get() == 1
        print(V.is_auto_update)
