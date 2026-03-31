# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:34:15 2020

@author: Balázs
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:35:05 2020

@author: Balázs
"""
# import libraries
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk

# set program directory
os.chdir("E:/Data Analysis/Python/Baking Bread")

#def calculateRecipe():
 #   return;

exec(open("programActions.py").read())

### RUN THE APP ###
window = tk.Tk()
window.title("Baking Bread v0.2 Developer Alpha")
exec(open("defineVars.py").read())
exec(open("ui_items.py").read())
exec(open("ui_placement.py").read())
exec(open("defaultValues.py").read())
window.mainloop()
