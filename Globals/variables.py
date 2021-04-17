from Utils.limits import get_saved_limits_or_empty_limits
from Utils.get_last_graphing_method import get_last_graphing_method

# GLOBAL VARIABLES THAT ARE USED ALL AROUND THE PROJECT
class Variables:
    currentMethod = get_last_graphing_method()

    cache = [[], []]
    live_noise = []
    changes_cache = []

    start_angle = 90

    limits = get_saved_limits_or_empty_limits()

    isAutoUpdate = True


