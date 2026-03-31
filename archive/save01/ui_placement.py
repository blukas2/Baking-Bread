# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:39:20 2020

@author: Balázs
"""

rowNumPerc = 0
lbl_bakersperc.grid(row = rowNumPerc, column = 0, columnspan = 2)
rowNumPerc = rowNumPerc + 1

s_perc_top.grid(row = rowNumPerc, column = 0, columnspan = 2, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_flourTypesPerc.grid(row = rowNumPerc, column = 0, columnspan = 2)
rowNumPerc = rowNumPerc + 1
drp_flourTypePerc1.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_flourTypePerc1.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourTypePerc2.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_flourTypePerc2.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourTypePerc3.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_flourTypePerc3.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s_perc2.grid(row = rowNumPerc, column = 0, columnspan = 2, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_hydration.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_hydration.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

drp_hydrationTypePerc1.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_hydrationTypePerc1.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_hydrationTypePerc2.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_hydrationTypePerc2.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

lbl_salt.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_salt.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
lbl_fat.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_fat.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s1.grid(row = rowNumPerc, column = 0, columnspan = 2, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_leavenShare.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_leavenShare.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
lbl_leavenHydration.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_leavenHydration.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
lbl_flourTypesLeaven.grid(row = rowNumPerc, column = 0, columnspan = 2)
rowNumPerc = rowNumPerc + 1
drp_flourTypeLeaven1.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_flourTypeLeaven1.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1
drp_flourTypeLeaven2.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_flourTypeLeaven2.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s2.grid(row = rowNumPerc, column = 0, columnspan = 2, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

lbl_loafWeight.grid(row = rowNumPerc, column = 0, columnspan = 1)
e_loafWeight.grid(row = rowNumPerc, column = 1, columnspan = 1)
rowNumPerc = rowNumPerc + 1

s3.grid(row = rowNumPerc, column = 0, columnspan = 2, sticky = 'ew')
rowNumPerc = rowNumPerc + 1

btn_calculateRec.grid(row = rowNumPerc, column = 0, columnspan = 2) 

# separator vertical
s_v.grid(row = 0, column = 3, rowspan = 17, sticky = 'ns')


# Ingredients
rowNumIng = 0
lbl_ingredients.grid(row = rowNumIng, column = 4, columnspan = 2)
rowNumIng = rowNumIng + 1

s_ing_top.grid(row = rowNumIng, column = 4, columnspan = 2, sticky = 'ew')
rowNumIng = rowNumIng + 1

# Ingredients/amounts
lbl_flourTypesIng.grid(row = rowNumIng, column = 4, columnspan = 2, sticky = 'ew')
rowNumIng = rowNumIng + 1
#drp_flourTypeIng1.grid(row = rowNumIng, column = 4, columnspan = 1, sticky = 'ew')
e_flourTypeIng1.grid(row = rowNumIng, column = 5, columnspan = 1, sticky = 'ew')
rowNumIng = rowNumIng + 1
#drp_flourTypeIng2.grid(row = rowNumIng, column = 4, columnspan = 1, sticky = 'ew')
e_flourTypeIng2.grid(row = rowNumIng, column = 5, columnspan = 1, sticky = 'ew')
rowNumIng = rowNumIng + 1
#drp_flourTypeIng3.grid(row = rowNumIng, column = 4, columnspan = 1, sticky = 'ew')
e_flourTypeIng3.grid(row = rowNumIng, column = 5, columnspan = 1, sticky = 'ew')
rowNumIng = rowNumIng + 1

s_ing2.grid(row = rowNumIng, column = 4, columnspan = 2, sticky = 'ew')
rowNumIng = rowNumIng + 1

lbl_liquid.grid(row = rowNumIng, column = 4, columnspan = 1)
e_liquid.grid(row = rowNumIng, column = 5, columnspan = 1)
rowNumIng = rowNumIng + 1
lbl_saltG.grid(row = rowNumIng, column = 4, columnspan = 1)
e_saltG.grid(row = rowNumIng, column = 5, columnspan = 1)
rowNumIng = rowNumIng + 1
lbl_fatG.grid(row = rowNumIng, column = 4, columnspan = 1)
e_fatG.grid(row = rowNumIng, column = 5, columnspan = 1)
rowNumIng = rowNumIng + 1
lbl_leavenAmount.grid(row = rowNumIng, column = 4, columnspan = 1)
e_leavenAmount.grid(row = rowNumIng, column = 5, columnspan = 1)
rowNumIng = rowNumIng + 1

s4.grid(row = rowNumIng, column = 4, columnspan = 2, sticky = 'ew')
rowNumIng = rowNumIng + 1

btn_calculatePerc.grid(row = rowNumIng, column = 4, columnspan = 2)
