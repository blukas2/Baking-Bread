# -*- coding: utf-8 -*-

# import libraries
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
import pandas as pd
pd.set_option('display.max_rows', 6)
import shutil

# set program directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#def calculateRecipe():
 #   return;

exec(open("programActions.py").read())

### RUN THE APP ###
window = tk.Tk()
window.title("Baking Bread v0.2 Developer Alpha")
#exec(open("programActions.py").read())
exec(open("defineVars.py").read())
exec(open("ui_items.py").read())
exec(open("ui_placement.py").read())
exec(open("defaultValues.py").read())
window.mainloop()
