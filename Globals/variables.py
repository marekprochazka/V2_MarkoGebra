from Utils.limits import get_saved_limits_or_empty_limits



# GLOBAL VARIABLES THAT ARE USED ALL AROUND THE PROJECT
class Variables:
    to_animate = None

    command_history = []
    history_moves = 0

    cache = [[], []]
    live_noise = []
    changes_cache = []

    start_angle = 90
    # noises = [[[0, 0, ".", "#fff", 1], [0, 0, ".", "#fff", 1]]]

    limits = get_saved_limits_or_empty_limits()

    is_auto_update = True



