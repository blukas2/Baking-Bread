# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:39:05 2020

@author: Balázs
"""

# Bakers percentagaes
lbl_bakersperc = tk.Label(text="Bakers percentages")
#lbl_bakersperc.config(anchor = CENTER, font=('Arial', 10))
lbl_bakersperc.config(anchor = CENTER, font=titleFont)

s_perc_top = ttk.Separator(window, orient=HORIZONTAL)

lbl_flourTypesPerc = tk.Label(text="Flour types")
drp_flourTypePerc1 = OptionMenu(window, flourTypePerc1, *flourTypeList)
e_flourTypePerc1 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypePerc2 = OptionMenu(window, flourTypePerc2, *flourTypeList)
e_flourTypePerc2 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypePerc3 = OptionMenu(window, flourTypePerc3, *flourTypeList)
e_flourTypePerc3 = Entry(window, width = 10, borderwidth = 5)

s_perc2 = ttk.Separator(window, orient=HORIZONTAL)

lbl_hydration = tk.Label(text="Hydration")
e_hydration = Entry(window, width = 10, borderwidth = 5)
drp_hydrationTypePerc1 = OptionMenu(window, hydrationTypePerc1, *hydrationTypeList)
e_hydrationTypePerc1 = Entry(window, width = 10, borderwidth = 5)
drp_hydrationTypePerc2 = OptionMenu(window, hydrationTypePerc2, *hydrationTypeList)
e_hydrationTypePerc2 = Entry(window, width = 10, borderwidth = 5)
lbl_salt = tk.Label(text="Salt")
e_salt = Entry(window, width = 10, borderwidth = 5)
lbl_fat = tk.Label(text="Fat")
e_fat = Entry(window, width = 10, borderwidth = 5)

s1 = ttk.Separator(window, orient=HORIZONTAL)

# Bakers percentagaes/Leaven
lbl_leavenShare = tk.Label(text="Leaven")
e_leavenShare = Entry(window, width = 10, borderwidth = 5)
lbl_leavenHydration = tk.Label(text="Leaven hydration")
e_leavenHydration = Entry(window, width = 10, borderwidth = 5)
lbl_flourTypesLeaven = tk.Label(text="Leaven flour")
drp_flourTypeLeaven1 = OptionMenu(window, flourTypeLeaven1, *flourTypeList)
e_flourTypeLeaven1 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypeLeaven2 = OptionMenu(window, flourTypeLeaven2, *flourTypeList)
e_flourTypeLeaven2 = Entry(window, width = 10, borderwidth = 5)

s2 = ttk.Separator(window, orient=HORIZONTAL)

# Bakers percentagaes/Loaf
lbl_loafWeight = tk.Label(text="Loaf weight (g)")
e_loafWeight = Entry(window, width = 10, borderwidth = 5)

s3 = ttk.Separator(window, orient=HORIZONTAL)

btn_calculateRec = tk.Button(window, text="Calculate recipe", command=calculateRecipe)

# Separator vertical
s_v = ttk.Separator(window, orient=VERTICAL)

# Ingredients
lbl_ingredients = tk.Label(text="Ingredients (g)")
lbl_ingredients.config(anchor = CENTER, font=titleFont)

s_ing_top = ttk.Separator(window, orient=HORIZONTAL)

lbl_flourTypesIng = tk.Label(text="Flour types")
drp_flourTypeIng1 = OptionMenu(window, flourTypeIng1, *flourTypeList)
e_flourTypeIng1 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypeIng2 = OptionMenu(window, flourTypeIng2, *flourTypeList)
e_flourTypeIng2 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypeIng3 = OptionMenu(window, flourTypeIng3, *flourTypeList)
e_flourTypeIng3 = Entry(window, width = 10, borderwidth = 5)

s_ing2 = ttk.Separator(window, orient=HORIZONTAL)


# Ingredients/amounts
lbl_liquid = tk.Label(text="Liquid")
e_liquid = Entry(window, width = 10, borderwidth = 5)
lbl_saltG = tk.Label(text="Salt")
e_saltG = Entry(window, width = 10, borderwidth = 5)
lbl_fatG = tk.Label(text="Fat")
e_fatG = Entry(window, width = 10, borderwidth = 5)
lbl_leavenAmount = tk.Label(text="Leaven")
e_leavenAmount = Entry(window, width = 10, borderwidth = 5)

s4 = ttk.Separator(window, orient=HORIZONTAL)

btn_calculatePerc = tk.Button(window, text="Calculate percentages", command=calculatePerc)

