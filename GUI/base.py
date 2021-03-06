from tkinter import Tk, OUTSIDE, Canvas, END
from tkinter import ttk as t

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

from Bases import BaseLabel
from Data.path import get_data_path
from Graphing.setup import graphFigure
from Static.constants import MAX_HEIGHT, MAX_WIDTH, MIN, MAX, X, Y, AVALIBLE_STYLES, NAME, INFO
from .pages import Mathematical, Pie, Bar, Noise
from Static.get_static_path import get_static_path
from Static.constants import MATH, PIE, BAR, NOISE

from Globals.variables import Variables as V


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
        self.iconbitmap(get_static_path() + "\\images\\logo.ico")
        self.main = main

        # TUPLE OF ALL GRAPHING METHOD FRAMES THAT IS REPRESENTED IN FE BY MULTISESECT
        self.method_components = (Mathematical, Pie, Bar, Noise)
        self.CONSTANTS_TO_METHOD_COMPONENTS = {MATH: Mathematical, PIE: Pie, BAR: Bar, NOISE: Noise}

        # RELATIVE CONTAINER TO WHICH IS WRITTEN PARTICULAR GRAPHING METHOD FRAME
        self.frame_methodContainer = t.Frame(self, width=MAX_WIDTH, height=MAX_HEIGHT)

        self.frame_methodContainer.pack(side="top", fill="both", expand=True)

        self.frame_methodContainer.grid_rowconfigure(0, weight=1)
        self.frame_methodContainer.grid_columnconfigure(0, weight=1)

        # MATLOPLIB GRAPH REPESENTATION ON FE
        canvas_graph = FigureCanvasTkAgg(graphFigure, self)
        canvas_graph.draw()
        canvas_graph.get_tk_widget().place(bordermode=OUTSIDE, x=MAX_WIDTH - 770, y=MAX_HEIGHT - 770)

        # MULTISELECT OF GRAPHING METHODS
        # AFTER SELECTION THE "show_Setup_Frame" FUNCTION FROM "new_show_frame.py" IS CALLED TO MANAGE FRAME CHANGE
        self.combobox_FrameSelector = t.Combobox(self, values=["Matematické", "Koláč", "Sloupcový", "Náhodný šum"],
                                                 state="readonly")
        self.combobox_FrameSelector.bind('<<ComboboxSelected>>',
                                         lambda event: self.__frame_change(
                                             self.method_components[self.combobox_FrameSelector.current()]))
        self.combobox_FrameSelector.current(list(self.CONSTANTS_TO_METHOD_COMPONENTS.keys()).index(V.currentMethod))
        self.combobox_FrameSelector.place(bordermode=OUTSIDE, width=MAX_WIDTH * .15, height=MAX_HEIGHT * .05,
                                          x=MAX_WIDTH * .01, y=MAX_HEIGHT * .05)

        # TOPRIGHT BUTTONS
        self.label_graphstyle = BaseLabel(self, text="Styl grafu:")
        self.label_graphstyle.place(bordermode=OUTSIDE, x=MAX_WIDTH * .595, width=MAX_WIDTH * .05, y=0,
                                    height=MAX_HEIGHT * .04)
        self.combobox_graphstyle = t.Combobox(self, values=AVALIBLE_STYLES, state="readonly")
        self.combobox_graphstyle.current(AVALIBLE_STYLES.index(self.__get_last_graph_style()))
        self.combobox_graphstyle.place(bordermode=OUTSIDE, x=MAX_WIDTH * .64, width=MAX_WIDTH * .1, y=0,
                                       height=MAX_HEIGHT * .04)
        self.combobox_graphstyle.bind("<<ComboboxSelected>>", self.__graph_pick_callback)
        self.hint = t.Button(self, command=lambda: self.openHelp(), text="Nápověda")
        self.hint.place(bordermode=OUTSIDE, x=MAX_WIDTH * .94, width=MAX_WIDTH * .06, y=0, height=MAX_HEIGHT * .04)
        self.button_saveAsImage = t.Button(self, text="uložit jako orázek", command=lambda: self.saver())
        self.button_saveAsImage.place(bordermode=OUTSIDE, x=MAX_WIDTH * .84, width=MAX_WIDTH * .1, y=0,
                                      height=MAX_HEIGHT * .04)
        self.button_deleteAll = t.Button(self, text="Smazat vše", command=lambda: self.delete_all())
        self.button_deleteAll.place(bordermode=OUTSIDE, x=MAX_WIDTH * .74, width=MAX_WIDTH * .1, y=0,
                                    height=MAX_HEIGHT * .04)

        self.container_listView = t.Frame(self)
        self.canvas_listView = Canvas(self.container_listView)
        self.scrollbar_listView = t.Scrollbar(self.container_listView, orient="vertical",
                                              command=self.canvas_listView.yview)
        self.frame_scrollable_listView = t.Frame(self.canvas_listView)
        self.frame_scrollable_listView.bind("<Configure>", lambda e: self.canvas_listView.configure(
            scrollregion=self.canvas_listView.bbox("all")))
        self.canvas_listView.create_window((0, 0), window=self.frame_scrollable_listView, anchor="nw")
        self.canvas_listView.configure(yscrollcommand=self.scrollbar_listView.set)

        self.container_listView.place(bordermode=OUTSIDE, x=MAX_WIDTH * .01, y=MAX_HEIGHT * .6, width=MAX_WIDTH * .4,
                                      height=MAX_HEIGHT * .3)
        self.canvas_listView.pack(side="left", fill="both", expand=True)
        self.scrollbar_listView.pack(side="right", fill="y")
        self.main.update_list_view()

        # RELATIVE FRAMES

        self.SetupFrames = {}

        self._frame = None
        self.show_methodFrame(component=self.CONSTANTS_TO_METHOD_COMPONENTS[V.currentMethod])

    def set_limits_entries_values_by_global_variables(self):
        for e in (self._frame.limits_settings.entry_minXLimit, self._frame.limits_settings.entry_maxXLimit,
                  self._frame.limits_settings.entry_minYLimit, self._frame.limits_settings.entry_maxYLimit):
            e.delete(0, END)

        self._frame.limits_settings.entry_minXLimit.insert(0, V.limits[X][MIN])
        self._frame.limits_settings.entry_maxXLimit.insert(0, V.limits[X][MAX])
        self._frame.limits_settings.entry_minYLimit.insert(0, V.limits[Y][MIN])
        self._frame.limits_settings.entry_maxYLimit.insert(0, V.limits[Y][MAX])

    def __frame_change(self, *args, **kwargs):
        self.show_methodFrame(*args, **kwargs)

    # AUTO UPDATE VARIABLE CONTROLLER
    def switch_auto_limit_update_value(self):
        V.isAutoUpdate = self.variable_isAutoUpdate.get() == 1
        print(V.isAutoUpdate)

    def __get_last_graph_style(self):
        with open(get_data_path() + "\\data.json") as f:
            data = json.load(f)
            return data["graphstyle"]

    def __graph_pick_callback(self, *args, **kwargs):
        msg = {NAME: "Upozornění", INFO: "Pro aktualizování stylu je třeba restartovat aplikaci."}
        self.main.restart_popup(info=True, error=msg, restart=True)
        with open(get_data_path() + "\\data.json", "r+") as f:
            data = json.load(f)
            data["graphstyle"] = self.combobox_graphstyle.get()
            f.seek(0)
            json.dump(data, f)
            f.truncate()

