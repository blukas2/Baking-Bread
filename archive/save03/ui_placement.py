# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:39:20 2020

@author: Balázs
"""

colNumNames = 0
colNumPerc = 1
colNumWeight = 2
colNumRecipes = colNumWeight + 2


rowNumPerc = 0
btn_showCard.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
lbl_bakersperc.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
lbl_weight.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc1.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

drp_flourType1.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_flourTypePerc1.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_flourTypeWeight1.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourType2.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_flourTypePerc2.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_flourTypeWeight2.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourType3.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_flourTypePerc3.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_flourTypeWeight3.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc2.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_hydration.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_hydrationPerc.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_hydrationWeight.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_hydrationType1.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_hydrationTypePerc1.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_hydrationTypeWeight1.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_hydrationType2.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_hydrationTypePerc2.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_hydrationTypeWeight2.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc3.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_fat.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_fatPerc.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_fatWeight.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_fatType1.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_fatTypePerc1.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_fatTypeWeight1.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_fatType2.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_fatTypePerc2.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_fatTypeWeight2.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc4.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_salt.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_saltPerc.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_saltWeight.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc5.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

drp_sugarType.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_sugarPerc.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_sugarWeight.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1


s_h_calc6.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_leavenShare.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_leavenShare.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_leavenAmount.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
lbl_leavenHydration.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_leavenHydration.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourTypeLeaven1.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_flourTypeLeaven1.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourTypeLeaven2.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_flourTypeLeaven2.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc7.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_loafWeight.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_loafWeight.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc8.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

btn_calculateRec.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1) 
btn_calculatePerc.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)

s_v1.grid(row = 0, column = colNumWeight+1, rowspan = rowNumPerc+1, sticky = 'ns')

rowNumPerc = rowNumPerc + 1
s_h_calc9.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')


################################################
################# Recipe list ##################
################################################

lbl_recipeList.grid(row = 0, column = colNumRecipes, columnspan = 4)


lb_recipes.grid(row = 2, column = colNumRecipes, columnspan = 4, rowspan = 5, sticky = "nsew")

btn_saveRecipeAs.grid(row = 7, column = colNumRecipes, columnspan = 1)
btn_saveRecipe.grid(row = 7, column = colNumRecipes+1, columnspan = 1)
btn_deleteRecipe.grid(row = 7, column = colNumRecipes+2, columnspan = 1)
btn_renameRecipe.grid(row = 7, column = colNumRecipes+3, columnspan = 1)

btn_updateDataset.grid(row = 8, column = colNumRecipes, columnspan = 4, sticky = "ew")

lbl_comments.grid(row = 10, column = colNumRecipes, columnspan = 5)
txt_comments.grid(row = 11, column = colNumRecipes, columnspan = 5, rowspan = 7, sticky = "nsew")