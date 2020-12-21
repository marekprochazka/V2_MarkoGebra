from matplotlib.figure import Figure

#SETUP VALUES FOR MAPLOTLIB GRAPH
f = Figure(figsize=(7.7, 7.7), dpi=100)
a = f.add_subplot(111)

a.grid(color='k', linestyle='-', linewidth=0.1)
a.set_axisbelow(True)
