from matplotlib.figure import Figure

f = Figure(figsize=(4.5, 4.5), dpi=100)
a = f.add_subplot(111)

a.grid(color='k', linestyle='-', linewidth=0.1)
a.set_axisbelow(True)

a.set_ylim(-10, 10)

lim1 = 30
lim2 = -30