# -*- coding: utf-8 -*-

lbl_bakersperc.grid(row = 0, column = 0, columnspan = 2)

s_perc_top.grid(row = 1, column = 0, columnspan = 2, sticky = 'ew')

lbl_flourTypesPerc.grid(row = 2, column = 0, columnspan = 2)
drp_flourTypePerc1.grid(row = 3, column = 0, columnspan = 1)
e_flourTypePerc1.grid(row = 3, column = 1, columnspan = 1)
drp_flourTypePerc2.grid(row = 4, column = 0, columnspan = 1)
e_flourTypePerc2.grid(row = 4, column = 1, columnspan = 1)
drp_flourTypePerc3.grid(row = 5, column = 0, columnspan = 1)
e_flourTypePerc3.grid(row = 5, column = 1, columnspan = 1)

s_perc2.grid(row = 6, column = 0, columnspan = 2, sticky = 'ew')

lbl_hydration.grid(row = 7, column = 0, columnspan = 1)
e_hydration.grid(row = 7, column = 1, columnspan = 1)
lbl_salt.grid(row = 8, column = 0, columnspan = 1)
e_salt.grid(row = 8, column = 1, columnspan = 1)
lbl_fat.grid(row = 9, column = 0, columnspan = 1)
e_fat.grid(row = 9, column = 1, columnspan = 1)

s1.grid(row = 10, column = 0, columnspan = 2, sticky = 'ew')

lbl_leavenShare.grid(row = 11, column = 0, columnspan = 1)
e_leavenShare.grid(row = 11, column = 1, columnspan = 1)
lbl_leavenHydration.grid(row = 12, column = 0, columnspan = 1)
e_leavenHydration.grid(row = 12, column = 1, columnspan = 1)
drp_flourTypeLeaven1.grid(row = 13, column = 0, columnspan = 1)

s2.grid(row = 14, column = 0, columnspan = 2, sticky = 'ew')

lbl_loafWeight.grid(row = 15, column = 0, columnspan = 1)
e_loafWeight.grid(row = 15, column = 1, columnspan = 1)

s3.grid(row = 16, column = 0, columnspan = 2, sticky = 'ew')

btn_calculateRec.grid(row = 17, column = 0, columnspan = 2) 

# separator vertical
s_v.grid(row = 0, column = 3, rowspan = 17, sticky = 'ns')

lbl_ingredients.grid(row = 0, column = 4, columnspan = 2)

s0.grid(row = 1, column = 4, columnspan = 2, sticky = 'ew')

lbl_flour.grid(row = 2, column = 4, columnspan = 1)
e_flour.grid(row = 2, column = 5, columnspan = 1)
lbl_liquid.grid(row = 3, column = 4, columnspan = 1)
e_liquid.grid(row = 3, column = 5, columnspan = 1)
lbl_saltG.grid(row = 4, column = 4, columnspan = 1)
e_saltG.grid(row = 4, column = 5, columnspan = 1)
lbl_fatG.grid(row = 6, column = 4, columnspan = 1)
e_fatG.grid(row = 6, column = 5, columnspan = 1)
lbl_leavenAmount.grid(row = 7, column = 4, columnspan = 1)
e_leavenAmount.grid(row = 7, column = 5, columnspan = 1)

s4.grid(row = 10, column = 4, columnspan = 2, sticky = 'ew')

btn_calculatePerc.grid(row = 12, column = 4, columnspan = 2)
