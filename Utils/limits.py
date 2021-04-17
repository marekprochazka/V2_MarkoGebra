from Static.constants import X, Y, MIN, MAX
from Data.path import get_data_path
import json

def get_saved_limits_or_empty_limits():
    with open(get_data_path() + "\\data.json") as f:
        data = json.load(f)
        limits = data["math_limits"]
        if limits:
            return limits
        return {
            X: {
                MIN: -30,
                MAX: 30
            },
            Y: {
                MIN: -30,
                MAX: 30
            }
        }

def save_limits_JSON_memory(limits):
    with open(get_data_path() + "\\data.json", "r+") as f:
        data = json.load(f)
        data["math_limits"] = limits
        f.seek(0)
        json.dump(data,f)
        f.truncate()

