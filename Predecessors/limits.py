from Globals.variables import Variables as V
from Static.constants import X, Y, MIN, MAX
from Decorators.input_checkers import check_limits_input


# MANUAL AND AUTO LIMIT UPDATES
class Limits:
    def __init__(self, main):
        self.main = main

    @check_limits_input
    def update_limits(self, min_x, max_x, min_y, max_y):
        return {
            X: {
                MIN: min_x,
                MAX: max_x
            },
            Y: {
                MIN: min_y,
                MAX: max_y
            }}

    def auto_update_limits_by_scatter_input(self, x, y):
        if x > V.limits[X][MAX]:
            V.limits[X][MAX] = x + 5
            V.limits[Y][MAX] = x + 5
            V.limits[X][MIN] = -x - 5
            V.limits[Y][MIN] = -x - 5

        if x < V.limits[X][MIN]:
            V.limits[X][MIN] = x - 5
            V.limits[Y][MIN] = x - 5
            V.limits[X][MAX] = -x + 5
            V.limits[Y][MAX] = -x + 5

        if y > V.limits[Y][MAX]:
            V.limits[X][MAX] = y + 5
            V.limits[Y][MAX] = y + 5
            V.limits[X][MIN] = -y - 5
            V.limits[Y][MIN] = -y - 5
        if y < V.limits[Y][MIN]:
            V.limits[X][MIN] = y - 5
            V.limits[Y][MIN] = y - 5
            V.limits[X][MAX] = -y + 5
            V.limits[Y][MAX] = -y + 5

        # FE UPDATE
        self.main.set_limits_entries_values_by_global_variables()
