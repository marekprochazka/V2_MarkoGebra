from matplotlib.figure import Figure
from matplotlib import style as st
from Data.path import get_path
#SETUP VALUES FOR MAPLOTLIB GRAPH
with open(get_path() + "\\graphstyle.txt") as data:
    style = data.read()
st.use(style)
f = Figure(figsize=(7.7, 7.7), dpi=100)
a = f.add_subplot(111)

a.grid(color='k', linestyle='-', linewidth=0.1)
a.set_axisbelow(True)
