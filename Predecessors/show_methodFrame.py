from Globals.variables import Variables as V
from Static.constants import MAX_WIDTH, MAX_HEIGHT, MATH, TO_ANIMATExTABLES, NOISE
from Data.functions import UPDATE_FUNCTIONS, get_tables
from Utils.load_noise_data import load_noise_data


# ONE OF THE MOST IMPORTANT FUNCTIONALITIES
# IS CALLED EVERY TIME A FRAME (GRAPHING METHOD) IS CHANGED
class ShowFrame:
    def __init__(self, main):
        self.main = main

    def show_methodFrame(self, component=None, exit=False):
        # SAVING PREVIOUS
        if V.currentMethod != None: UPDATE_FUNCTIONS[V.currentMethod](V.changes_cache)
        if V.currentMethod == MATH:
            from Utils.limits import save_limits_JSON_memory
            save_limits_JSON_memory(V.limits)

        # CLEAR changes_cache
        V.changes_cache = []
        if not exit:
            # CHANGE to_animate TO ACTUAL FRAME + FRAME DRAWING
            if component != None:

                if self.main._frame is not None:
                    self.main._frame.destroy()
                self.main._frame = component(self.main.frame_methodContainer, self.main)
                V.currentMethod = self.main._frame.type
                self.main._frame.place(x=MAX_WIDTH * .01, y=MAX_HEIGHT * .15, height=MAX_HEIGHT * 45,
                                       width=MAX_WIDTH * .40)

            # LOADING DATA TO CACHE
            if V.currentMethod != NOISE:
                V.cache = list(get_tables(TO_ANIMATExTABLES[V.currentMethod]))
            else:
                V.cache = load_noise_data(list(get_tables(TO_ANIMATExTABLES[V.currentMethod])))

            # UPDATE LIMITS IF IT'S MATH GRAPHING
            if V.currentMethod == MATH and V.isAutoUpdate:
                for value in V.cache[0]:
                    self.main.auto_update_limits_by_scatter_input(value[1], value[2])

            # TABLE DATA WRITING
            self.main.update_list_view()

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
