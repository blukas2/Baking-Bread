# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:39:05 2020

@author: Balázs
"""
# designing variables
drpSelectorWidth = 16

# show card button
btn_showCard = tk.Button(window, text="Show card", command=showCard)

# Titles
lbl_bakersperc = tk.Label(text="Baker's %")
lbl_bakersperc.config(anchor = CENTER, font=titleFont)
lbl_weight = tk.Label(text="Weight (g)")
lbl_weight.config(anchor = CENTER, font=titleFont)

s_h_calc1 = ttk.Separator(window, orient=HORIZONTAL)

# Flour types
drp_flourType1 = OptionMenu(window, flourType1, *flourTypeList)
drp_flourType1.config(width=drpSelectorWidth)
e_flourTypePerc1 = Entry(window, width = 10, borderwidth = 5)
e_flourTypeWeight1 = Entry(window, width = 10, borderwidth = 5)
drp_flourType2 = OptionMenu(window, flourType2, *flourTypeList)
drp_flourType2.config(width=drpSelectorWidth)
e_flourTypePerc2 = Entry(window, width = 10, borderwidth = 5)
e_flourTypeWeight2 = Entry(window, width = 10, borderwidth = 5)
drp_flourType3 = OptionMenu(window, flourType3, *flourTypeList)
drp_flourType3.config(width=drpSelectorWidth)
e_flourTypePerc3 = Entry(window, width = 10, borderwidth = 5)
e_flourTypeWeight3 = Entry(window, width = 10, borderwidth = 5)

s_h_calc2 = ttk.Separator(window, orient=HORIZONTAL)

# hydration
lbl_hydration = tk.Label(text="Hydration")
e_hydrationPerc = Entry(window, width = 10, borderwidth = 5)
e_hydrationWeight = Entry(window, width = 10, borderwidth = 5)
drp_hydrationType1 = OptionMenu(window, hydrationType1, *hydrationTypeList)
drp_hydrationType1.config(width=drpSelectorWidth)
e_hydrationTypePerc1 = Entry(window, width = 10, borderwidth = 5)
e_hydrationTypeWeight1 = Entry(window, width = 10, borderwidth = 5)
drp_hydrationType2 = OptionMenu(window, hydrationType2, *hydrationTypeList)
drp_hydrationType2.config(width=drpSelectorWidth)
e_hydrationTypePerc2 = Entry(window, width = 10, borderwidth = 5)
e_hydrationTypeWeight2 = Entry(window, width = 10, borderwidth = 5)

s_h_calc3 = ttk.Separator(window, orient=HORIZONTAL)

lbl_fat = tk.Label(text="Fat")
e_fatPerc = Entry(window, width = 10, borderwidth = 5)
e_fatWeight = Entry(window, width = 10, borderwidth = 5)
drp_fatType1 = OptionMenu(window, fatType1, *fatTypeList)
drp_fatType1.config(width=drpSelectorWidth)
e_fatTypePerc1 = Entry(window, width = 10, borderwidth = 5)
e_fatTypeWeight1 = Entry(window, width = 10, borderwidth = 5)
drp_fatType2 = OptionMenu(window, fatType2, *fatTypeList)
drp_fatType2.config(width=drpSelectorWidth)
e_fatTypePerc2 = Entry(window, width = 10, borderwidth = 5)
e_fatTypeWeight2 = Entry(window, width = 10, borderwidth = 5)

s_h_calc4 = ttk.Separator(window, orient=HORIZONTAL)

lbl_salt = tk.Label(text="Salt")
e_saltPerc = Entry(window, width = 10, borderwidth = 5)
e_saltWeight = Entry(window, width = 10, borderwidth = 5)

s_h_calc5 = ttk.Separator(window, orient=HORIZONTAL)

drp_sugarType = OptionMenu(window, sugarType, *sugarTypeList)
drp_sugarType.config(width=drpSelectorWidth)
e_sugarPerc = Entry(window, width = 10, borderwidth = 5)
e_sugarWeight = Entry(window, width = 10, borderwidth = 5)

s_h_calc6 = ttk.Separator(window, orient=HORIZONTAL)

# Bakers percentagaes/Leaven
lbl_leavenShare = tk.Label(text="Leaven")
e_leavenShare = Entry(window, width = 10, borderwidth = 5)
e_leavenAmount = Entry(window, width = 10, borderwidth = 5)
lbl_leavenHydration = tk.Label(text="Leaven hydration")
e_leavenHydration = Entry(window, width = 10, borderwidth = 5)
drp_flourTypeLeaven1 = OptionMenu(window, flourTypeLeaven1, *flourTypeList)
drp_flourTypeLeaven1.config(width=drpSelectorWidth)
e_flourTypeLeaven1 = Entry(window, width = 10, borderwidth = 5)
drp_flourTypeLeaven2 = OptionMenu(window, flourTypeLeaven2, *flourTypeList)
drp_flourTypeLeaven2.config(width=drpSelectorWidth)
e_flourTypeLeaven2 = Entry(window, width = 10, borderwidth = 5)

s_h_calc7 = ttk.Separator(window, orient=HORIZONTAL)

# Bakers percentagaes/Loaf
lbl_loafWeight = tk.Label(text="Loaf weight (g)")
e_loafWeight = Entry(window, width = 10, borderwidth = 5)

s_h_calc8 = ttk.Separator(window, orient=HORIZONTAL)

btn_calculateRec = tk.Button(window, text="Calculate weight", command=calculateRecipe)
btn_calculatePerc = tk.Button(window, text="Calculate %s", command=calculatePerc)

s_v1 = ttk.Separator(window, orient=VERTICAL)

s_h_calc9 = ttk.Separator(window, orient=HORIZONTAL)


################################################
################# Recipe list ##################
################################################

lbl_recipeList = tk.Label(text="Recipe List")
lbl_recipeList.config(anchor = CENTER, font=titleFont)


lb_recipes = tk.Listbox(window, height = 5, exportselection = False)
for i in breadDataset['breadName'].tolist():
    lb_recipes.insert(0, i)
lb_recipes.bind('<<ListboxSelect>>', breadSelect)    

btn_saveRecipe = tk.Button(window, text="Save", command=saveRecipe)
btn_saveRecipeAs = tk.Button(window, text="Save as..", command=saveRecipeAs)
btn_deleteRecipe = tk.Button(window, text="Delete", command=deleteRecipe)
btn_renameRecipe = tk.Button(window, text="Rename", command=renameRecipe)

btn_updateDataset = tk.Button(window, text="Update dataset", command=updateDataset)
    
#lb_recipes.insert(0, "Alapkenyer")


lbl_comments = tk.Label(text="Comments")
lbl_comments.config(anchor = CENTER, font=titleFont)
txt_comments = Text(window, width = 20, height = 5)