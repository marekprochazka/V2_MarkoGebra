from Static.constants import X, Y, MIN, MAX


class Variables:
    to_animate = None

    pie_colors = []

    command_history = []
    history_moves = 0

    cache = []
    changes_cache = []

    coordinates_scatter = []
    coordinates_plot = []
    coordinates_all_list = []

    slices = []
    cols = []
    activities = []
    explode = []
    start_angle = 90

    bars = []
    # [name,value,color]

    noises = [[[0, 0, ".", "#fff", 1], [0, 0, ".", "#fff", 1]]]
    dispersion = []
    number = []
    basic_gen = []

    lim1 = 30
    lim2 = -30

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
