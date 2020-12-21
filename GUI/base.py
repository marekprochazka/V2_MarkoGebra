from tkinter import Tk, OUTSIDE, Canvas, END
from tkinter import ttk as t

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graphing.setup import f
from Static.constants import MAX_HEIGHT, MAX_WIDTH, MIN, MAX, X, Y
from .pages import Mathematical, Pie, Bar, Noise


from Globals.variables import Variables as V

from Utils.entry_callbacks import is_digit_callback


# ALL GUI WORK IS SOMEHOW CONNECTED TO THIS (EXCEPTION: "new_show_frame.py")
# FRAMES TO DIFFERENT GRAPHING METHODS ARE CONNECTED TO THIS CLASS
# FRAME CHANGING LOGIC IS MANAGED IN "Predecessors/new_show_frame.py"
class Base(Tk):
    def __init__(self, main):
        # INITIAL GUI SETUP
        Tk.__init__(self)
        Tk.wm_title(self, "MarkoGebra")
        Tk.minsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        Tk.maxsize(self, width=MAX_WIDTH, height=MAX_HEIGHT)
        self.main = main

        # TUPLE OF ALL GRAPHING METHODS THAT IS REPRESENTED IN FE BY MULTISESECT
        self.input_frames = (Mathematical, Pie, Bar, Noise)

        # RELATIVE CONTAINER TO WHICH IS WRITTEN PARTICULAR GRAPHING METHOD
        self.SetupContainer = t.Frame(self, width=MAX_WIDTH, height=MAX_HEIGHT)

        self.SetupContainer.pack(side="top", fill="both", expand=True)

        self.SetupContainer.grid_rowconfigure(0, weight=1)
        self.SetupContainer.grid_columnconfigure(0, weight=1)

        # MATLOPLIB GRAPH REPESENTATION ON FE
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 770, y=MAX_HEIGHT - 770)

        # MULTISELECT OF GRAPHING METHODS
        # AFTER SELECTION THE "show_Setup_Frame" FUNCTION FROM "new_show_frame.py" IS CALLED TO MANAGE FRAME CHANGE
        self.CBB2 = t.Combobox(self, values=["Matematické", "Koláč", "Sloupcový","Náhodný šum"],
                               state="readonly")
        self.CBB2.bind('<<ComboboxSelected>>',
                       lambda event: self.__frame_change(self.input_frames[self.CBB2.current()]))
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


        self.list_view_container = t.Frame(self)
        self.list_view_canvas = Canvas(self.list_view_container)
        self.list_view_scrollbar = t.Scrollbar(self.list_view_container, orient="vertical", command=self.list_view_canvas.yview)
        self.list_view_scrollable_frame = t.Frame(self.list_view_canvas)
        self.list_view_scrollable_frame.bind("<Configure>", lambda e: self.list_view_canvas.configure(scrollregion=self.list_view_canvas.bbox("all")))
        self.list_view_canvas.create_window((0, 0), window=self.list_view_scrollable_frame, anchor="nw")
        self.list_view_canvas.configure(yscrollcommand=self.list_view_scrollbar.set)

        self.list_view_container.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .6, width=MAX_WIDTH * .4,
                                       height=MAX_HEIGHT * .3)
        self.list_view_canvas.pack(side="left", fill="both", expand=True)
        self.list_view_scrollbar.pack(side="right", fill="y")
        self.main.update_list_view()

        # RELATIVE FRAMES

        self.SetupFrames = {}

        self._frame = None
        self.show_Setup_Frame(component=Mathematical)

    def set_limits_entries_values_by_global_variables(self):

        for e in (self._frame.limits_settings.limits_entry_x_min, self._frame.limits_settings.limits_entry_x_max, self._frame.limits_settings.limits_entry_y_min, self._frame.limits_settings.limits_entry_y_max):
            e.delete(0, END)

        self._frame.limits_settings.limits_entry_x_min.insert(0, V.limits[X][MIN])
        self._frame.limits_settings.limits_entry_x_max.insert(0, V.limits[X][MAX])
        self._frame.limits_settings.limits_entry_y_min.insert(0, V.limits[Y][MIN])
        self._frame.limits_settings.limits_entry_y_max.insert(0, V.limits[Y][MAX])

    def __frame_change(self,*args,**kwargs):
        self.show_Setup_Frame(*args,**kwargs)




    # AUTO UPDATE VARIABLE CONTROLLER
    def switch_auto_limit_update_value(self):
        V.is_auto_update = self.limits_auto_update_checkbox_check_var.get() == 1
        print(V.is_auto_update)

