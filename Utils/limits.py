from Static.constants import X, Y, MIN, MAX
from Data.path import get_path
import json

def get_saved_limits_or_empty_limits():
    with open(get_path() + "\math_limits.json") as data:
        data = json.load(data)
        if data:
            return data
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
    with open(get_path()+"\math_limits.json","w") as data:
        json.dump(limits,data)