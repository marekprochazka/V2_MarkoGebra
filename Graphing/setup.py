from matplotlib.figure import Figure
from matplotlib import style as st
from Data.path import get_data_path
import json

#SETUP VALUES FOR MAPLOTLIB GRAPH
with open(get_data_path() + "\\data.json") as f:
    data = json.load(f)
    style = data["graphstyle"]
st.use(style)
graphFigure = Figure(figsize=(7.7, 7.7), dpi=100)
graphSubPlot = graphFigure.add_subplot(111)

graphSubPlot.grid(color='k', linestyle='-', linewidth=0.1)
graphSubPlot.set_axisbelow(True)
