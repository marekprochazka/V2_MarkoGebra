from Utils.limits import get_saved_limits_or_empty_limits


# GLOBAL VARIABLES THAT ARE USED ALL AROUND THE PROJECT
class Variables:
    currentMethod = None

    cache = [[], []]
    live_noise = []
    changes_cache = []

    start_angle = 90

    limits = get_saved_limits_or_empty_limits()

    isAutoUpdate = True
