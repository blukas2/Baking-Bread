# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:35:20 2020

@author: Balázs
"""

    
def calculateRecipe():
    g_flour = float(e_loafWeight.get())/(1+(float(e_leavenShare.get())/100*(2-float(e_leavenHydration.get())/100)/2))
    g_leaven = g_flour*float(e_leavenShare.get())/100
    g_liquid = float(e_loafWeight.get())*float(e_hydration.get())/100-g_leaven*(float(e_leavenHydration.get())/100/2)
    g_fat = (g_flour+g_leaven*(float(e_leavenHydration.get())/100/2))*(float(e_fat.get())/100)
    g_salt = float(e_loafWeight.get())*float(e_salt.get())/100    
#    e_flour.delete(0, END)
#    e_flour.insert(0, round(g_flour, 0))
    e_leavenAmount.delete(0, END)
    e_leavenAmount.insert(0, round(g_leaven, 0))
    e_liquid.delete(0, END)
    e_liquid.insert(0, round(g_liquid, 0))
    e_fatG.delete(0, END)
    e_fatG.insert(0, round(g_fat, 0))
    e_saltG.delete(0, END)
    e_saltG.insert(0, round(g_salt, 0))
    flourTypeIng1.set(flourTypePerc1.get())
    flourTypeIng2.set(flourTypePerc2.get())
    flourTypeIng3.set(flourTypePerc3.get())
    g_flourTypeIng1 = g_flour*float(e_flourTypePerc1.get())/100
    g_flourTypeIng2 = g_flour*float(e_flourTypePerc2.get())/100
    g_flourTypeIng3 = g_flour*float(e_flourTypePerc3.get())/100
    e_flourTypeIng1.delete(0, END)
    e_flourTypeIng1.insert(0, round(g_flourTypeIng1, 0))
    e_flourTypeIng2.delete(0, END)
    e_flourTypeIng2.insert(0, round(g_flourTypeIng2, 0))
    e_flourTypeIng3.delete(0, END)
    e_flourTypeIng3.insert(0, round(g_flourTypeIng3, 0))

def calculatePerc():
    return;
    
    
flourTypeList = ['NA', 'BL55 buzafinomliszt', 'BL80 kenyerliszt', 'TK buzaliszt',
                 'rozsliszt', 'TK rozsliszt', 'zabliszt']

hydrationTypeList = ['NA', 'gyumolcsle', 'joghurt', 'kokusztej', 'buzasor', 'tej',
                     'viz', 'zabtej']
