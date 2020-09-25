import numpy
class Variables:

    to_animate = 0

    pie_colors = []

    command_history = []
    history_moves = 0


    new_math = {"SC":numpy.empty((0,1))}
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