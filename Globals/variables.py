from Static.constants import X, Y, MIN, MAX


# GLOBAL VARIABLES THAT ARE USED ALL AROUND THE PROJECT
class Variables:
    to_animate = None

    command_history = []
    history_moves = 0

    cache = [[],[]]
    changes_cache = []

    start_angle = 90
    # noises = [[[0, 0, ".", "#fff", 1], [0, 0, ".", "#fff", 1]]]

    limits = {
        X: {
            MIN: -30,
            MAX: 30
        },
        Y: {
            MIN: -30,
            MAX: 30
        }
    }

    is_auto_update = True
