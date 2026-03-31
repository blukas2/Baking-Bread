# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:28:00 2020

@author: Balázs
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:11:40 2020

@author: Balázs
"""

# Generate recipe card
tlvl_recipeCard = Toplevel()
tlvl_recipeCard.title('Recipe card')
frm_ingredientList = Frame(tlvl_recipeCard)
frm_ingredientList.pack()
if float((e_flourTypeWeight1.get())) != 0:
        itemName = flourType1.get()
        itemAmount = e_flourTypeWeight1.get()
        lbl_item_flourType1 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_flourType1.pack()        
if float((e_flourTypeWeight2.get())) != 0:
        itemName = flourType2.get()
        itemAmount = e_flourTypeWeight2.get()
        lbl_item_flourType2 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_flourType2.pack()
if float((e_flourTypeWeight3.get())) != 0:
        itemName = flourType3.get()
        itemAmount = e_flourTypeWeight3.get()
        lbl_item_flourType3 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_flourType3.pack()
if float((e_hydrationTypeWeight1.get())) != 0:
        itemName = hydrationType1.get()
        itemAmount = e_hydrationTypeWeight1.get()
        lbl_item_hydrationType1 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_hydrationType1.pack()
if float((e_hydrationTypeWeight2.get())) != 0:
        itemName = hydrationType2.get()
        itemAmount = e_hydrationTypeWeight2.get()
        lbl_item_hydrationType2 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_hydrationType2.pack()
if float((e_fatTypeWeight1.get())) != 0:
        itemName = fatType1.get()
        itemAmount = e_fatTypeWeight1.get()
        lbl_item_fatType1 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_fatType1.pack()
if float((e_fatTypeWeight2.get())) != 0:
        itemName = fatType2.get()
        itemAmount = e_fatTypeWeight2.get()
        lbl_item_fatType2 = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_fatType2.pack()
if float((e_saltWeight.get())) != 0:
        itemName = "salt"
        itemAmount = e_saltWeight.get()
        lbl_item_salt = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_salt.pack()
if float((e_sugarWeight.get())) != 0:
        itemName = sugarType.get()
        itemAmount = e_sugarWeight.get()
        lbl_item_sugar = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_sugar.pack()
if float((e_sugarWeight.get())) != 0:
        itemName = sugarType.get()
        itemAmount = e_sugarWeight.get()
        lbl_item_sugar = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName]))
        lbl_item_sugar.pack()
if float((e_leavenAmount.get())) != 0:
        itemName = "leaven"
        itemAmount = e_leavenAmount.get()
        leavenHydrationNote = ''.join(['(',e_leavenHydration.get(), '%', ' ', 'hydration', ')'])
        lbl_item_leaven = tk.Label(tlvl_recipeCard, text = ' '.join([''.join([itemAmount, 'g']), itemName, leavenHydrationNote]))
        lbl_item_leaven.pack()
        