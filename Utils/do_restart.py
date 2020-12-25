import sys
import os

def do_restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)