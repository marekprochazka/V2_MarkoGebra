
MAX_WIDTH = 1600
MAX_HEIGHT = 600

FUNCTION_ALLOWED_MARKS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "+", "-", "*", "/", "(", ")","s","c","t","p"]

POINT_MARKERS = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
                 'X', 'D', 'd', '|', '_']

LINE_MARKERS = ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']

AVALIBLE_STYLES = ['Solarize_Light2', '_classic_test_patch', 'classic', 'dark_background',
                   'fivethirtyeight', 'ggplot', 'seaborn', 'seaborn-bright',
                   'seaborn-dark','seaborn-poster',
                   'seaborn-ticks', 'seaborn-whitegrid']

GRAPHING_METHOD = {
    "matematical": 1,
    "pie": 2,
    "bar": 3,
    "noise": 4
}

ACTION = "ACTION"
DATA = "DATA"
ID = "ID"
UPDATE = "UPDATE"
CREATE = "CREATE"
DELETE = "DELETE"
TYPE = "TYPE"
SCATTER = "SCATTER"
FUNCTION = "FUNCTION"