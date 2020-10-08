from Globals.variables import Variables as V
from Static.constants import MAX_WIDTH, MAX_HEIGHT, MATH, BAR, PIE, TO_ANIMATExTABLES
from Data.functions import UPDATE_FUNCTIONS, get_tables
from Utils.graph_update import *
from Static.constants import ACTION, CREATE, UPDATE, DELETE, ID, DATA, TYPE, SCATTER, FUNCTION
from Utils.uuid import generate_uuid, format_existing_uuid


# ONE OF THE MOST IMPORTANT FUNCTIONALITIES
# IS CALLED EVERY TIME A FRAME (GRAPHING METHOD) IS CHANGED
class ShowFrame:
    def __init__(self, main):
        self.main = main

    def show_Setup_Frame(self, cont=None):
        # SAVING PREVIOUS
        if V.to_animate != None: UPDATE_FUNCTIONS[V.to_animate](V.changes_cache)

        # CLEAR changes_cache
        V.changes_cache = []

        # CHANGE to_animate TO ACTUAL FRAME + FRAME DRAWING
        if cont != None:
            new_frame = cont(self.main.SetupContainer, self.main)
            V.to_animate = new_frame.type

            # TODO uncomment after GUI connection

            if self.main._frame is not None:
                for child in self.main._frame.winfo_children():
                    child.destroy()
                self.main._frame.destroy()
            self.main._frame = new_frame
            self.main._frame.place(x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15, height=MAX_HEIGHT * 45, width=MAX_WIDTH * .40)

        # LOADING DATA TO CACHE
        V.cache = list(get_tables(TO_ANIMATExTABLES[V.to_animate]))

        # UPDATE LIMITS IF IT'S MATH GRAPHING
        if V.to_animate == MATH:
            for value in V.cache[0]:
                self.main.auto_update_limits_by_scatter_input(value[1],value[2])

        # TABLE DATA WRITING
        self.main.update_table()

    def __update_limits(self):
        for scatter_value in V.cache[0]:
            if scatter_value[1] > V.lim1: V.lim1 = scatter_value[1]
            if scatter_value[1] < V.lim2: V.lim2 = scatter_value[1]
            if scatter_value[2] > V.lim1: V.lim1 = scatter_value[2]
            if scatter_value[2] < V.lim2: V.lim2 = scatter_value[2]

# TESTING
# tst = ShowFrame("aaaa")
# V.to_animate = MATH
# V.changes_cache.append({ACTION:CREATE,DATA:(1,2,":-)","red",7),ID:generate_uuid(),TYPE:SCATTER})
# V.changes_cache.append({ACTION:CREATE,DATA:("x**2","solid","red",2),ID:generate_uuid(),TYPE:FUNCTION})
# print((V.changes_cache))
# tst.show_Setup_Frame()
# import numpy
# V.to_animate = PIE
# print(V.cache)
# V.cache = list(get_tables(TO_ANIMATExTABLES[V.to_animate]))
# print(V.cache)
