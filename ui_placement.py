# -*- coding: utf-8 -*-

colNumNames = 0
colNumPerc = colNumNames + 1
colNumWeight = colNumNames + 2

colNumLeavenNames = colNumWeight + 2
colNumLeavenPerc = colNumLeavenNames + 1
colNumLeavenWeight = colNumLeavenNames + 2

colNumRecipes = colNumLeavenWeight + 2

################################################
################# Main Dough ###################
################################################

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

s_h_calc7.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_poolishShare.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_poolishShare.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_poolishAmount.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1
lbl_poolishHydration.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_poolishHydration.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc8.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_tangzhongShare.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_tangzhongShare.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
e_tangzhongAmount.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc9.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_loafWeight.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
e_loafWeight.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_h_calc10.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

btn_calculateAll.grid(row = rowNumPerc, column = colNumNames, columnspan = 1)
btn_calculateRec.grid(row = rowNumPerc, column = colNumPerc, columnspan = 1) 
btn_calculatePerc.grid(row = rowNumPerc, column = colNumWeight, columnspan = 1)

s_v1.grid(row = 0, column = colNumWeight+1, rowspan = rowNumPerc+1, sticky = 'ns')

rowNumPerc = rowNumPerc + 1
s_h_calc11.grid(row = rowNumPerc, column = colNumNames, columnspan = 3, sticky = 'ew')



################################################
################# Levain & poolish #############
################################################

rowNumLeaven = 0
################
### Leaven
#############
# Titles

lbl_prefrmtTitle.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
lbl_prefrmtBakersperc.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
lbl_prefrmtWeight.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1

s_h_prefrmtCalc1.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 3, sticky = 'ew')
rowNumLeaven = rowNumLeaven + 1

lbl_prefrmt_leaven.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 2)
e_prefrmt_leavenAmount.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
drp_flourTypeLeaven1.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_flourTypeLeaven1.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_flourTypeLeavenWeight1.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
drp_flourTypeLeaven2.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_flourTypeLeaven2.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_flourTypeLeavenWeight2.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 2
lbl_prefrmt_leavenHydration.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_prefrmt_leavenHydration.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_prefrmt_leavenHydrationWeight.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1

s_h_prefrmtCalc2.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 3, sticky = 'ew')
rowNumLeaven = rowNumLeaven + 1


lbl_prefrmt_poolish.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 2)
e_prefrmt_poolishAmount.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 2
drp_flourTypePoolish1.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_flourTypePoolish1.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_flourTypePoolishWeight1.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
drp_flourTypePoolish2.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_flourTypePoolish2.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_flourTypePoolishWeight2.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
lbl_prefrmt_poolishHydration.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_prefrmt_poolishHydration.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_prefrmt_poolishHydrationWeight.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 2
lbl_prefrmt_poolish_leavenShare.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_prefrmt_poolish_leavenShare.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
e_prefrmt_poolish_leavenAmount.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 2
lbl_prefrmt_poolish_leavenHydration.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_prefrmt_poolish_leavenHydration.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1



s_h_prefrmtCalc3.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 3, sticky = 'ew')
rowNumLeaven = rowNumLeaven + 1


lbl_prefrmt_tangzhong.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 2)
e_prefrmt_tangzhongAmount.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
drp_flourTypeTangzhong.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_flourTypeTangzhongWeight.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 2
lbl_prefrmt_tangzhongHydration.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
e_prefrmt_tangzhongHydrationWeight.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1


s_h_prefrmtCalc4.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 3, sticky = 'ew')
rowNumLeaven = rowNumLeaven + 1


btn_prefrmt_getAmounts.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)
btn_prefrmt_calculateWeights.grid(row = rowNumLeaven, column = colNumLeavenPerc, columnspan = 1)
btn_prefrmt_calculatePerc.grid(row = rowNumLeaven, column = colNumLeavenWeight, columnspan = 1)
rowNumLeaven = rowNumLeaven + 1
btn_prefrmt_addAmounts.grid(row = rowNumLeaven, column = colNumLeavenNames, columnspan = 1)




s_v2.grid(row = 0, column = colNumLeavenWeight+1, rowspan = rowNumPerc+1, sticky = 'ns')





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