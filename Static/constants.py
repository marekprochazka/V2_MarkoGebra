MAX_WIDTH = 1600
MAX_HEIGHT = 900


FUNCTION_ALLOWED_MARKS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "+", "-", "*", "/", "(", ")","s","c","t","p"]

POINT_MARKERS = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', '+', 'x',
                 'X', 'D', 'd', '|', '_']

LINE_MARKERS = ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']

AVALIBLE_STYLES = ['Solarize_Light2', '_classic_test_patch', 'classic', 'dark_background',
                   'fivethirtyeight', 'ggplot', 'seaborn', 'seaborn-bright',
                   'seaborn-dark','seaborn-poster',
                   'seaborn-ticks', 'seaborn-whitegrid']


BASIC_COLORS_VALUES = ["blue", "green", "red", "cyan", "purple", "gold", "black"]
BASIC_COLORS_NAMES = ["Modrá", "Zelená", "Červená", "Světle modrá", "Fialová", "Žlutá", "Černá"]


#NAMING CONSTANTS TO AVOID TYPOS
ACTION = "ACTION"
DATA = "DATA"
ID = "ID"
UPDATE = "UPDATE"
CREATE = "CREATE"
DELETE = "DELETE"
TYPE = "TYPE"
SCATTER = "SCATTER"
FUNCTION = "FUNCTION"
MATH = "MATH"
BAR = "BAR"
PIE = "PIE"
NOISE = "NOISE"
MIN = "MIN"
MAX = "MAX"
X = "X"
Y = "Y"


#RELATIONSHIP BETWEEN to_animate VALUES AND GRAPHING METHOD FORMATTED FOR DATABASE FUNCTIONS "Data\functions.py"
TO_ANIMATExTABLES = {
    MATH:("scatter","function"),
    BAR:("bar",),
    PIE:("pie",),
    NOISE:("noise",)
}

#DATA INPUTS
CACHE = "CACHE"
CHANGES_CACHE = "CHANGES_CACHE"
ERRORS = "ERRORS"
NAME = "NAME"
INFO = "INFO"

MAX_NOISE_DISPERSION = 100
MAX_NOISE_QUANTITY = 100
