# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:35:20 2020

@author: Balázs
"""

# Lists    
flourTypeList = ['NA', 'BL55 buzafinomliszt', 'BL80 kenyerliszt', 'rozsliszt', 
                 'TK buzaliszt', 'TK rozsliszt', 'zabliszt']

hydrationTypeList = ['NA', 'buzasor', 'gyumolcsle', 'joghurt', 'kokusztej', 'tej',
                     'viz', 'zabtej']

fatTypeList = ['NA', 'kokuszzsir', 'oliva olaj', 'tojas', 'vaj']

sugarTypeList = ['NA', 'barnacukor', 'kristalycukor', 'mez', 'nadcukor']


# Buttons    
def calculateRecipe():
    g_flour = float(e_loafWeight.get())/(1+(float(e_leavenShare.get())/100*(2-float(e_leavenHydration.get())/100)/2))
    g_leaven = g_flour*float(e_leavenShare.get())/100
    g_hydration = float(e_loafWeight.get())*float(e_hydrationPerc.get())/100-g_leaven*(float(e_leavenHydration.get())/100/2)
    g_fat = (g_flour+g_leaven*(float(e_leavenHydration.get())/100/2))*(float(e_fatPerc.get())/100)
    g_salt = float(e_loafWeight.get())*float(e_saltPerc.get())/100
    g_sugar = float(e_loafWeight.get())*float(e_sugarPerc.get())/100    
    e_leavenAmount.delete(0, END)
    e_leavenAmount.insert(0, round(g_leaven, 0))
    e_hydrationWeight.delete(0, END)
    e_hydrationWeight.insert(0, round(g_hydration, 0))
    e_fatWeight.delete(0, END)
    e_fatWeight.insert(0, round(g_fat, 0))
    e_saltWeight.delete(0, END)
    e_saltWeight.insert(0, round(g_salt, 0))
    e_sugarWeight.delete(0, END)
    e_sugarWeight.insert(0, round(g_sugar, 0))
    g_flourTypeWeight1 = g_flour*float(e_flourTypePerc1.get())/100
    g_flourTypeWeight2 = g_flour*float(e_flourTypePerc2.get())/100
    g_flourTypeWeight3 = g_flour*float(e_flourTypePerc3.get())/100
    g_hydrationType1 = g_hydration*(float(e_hydrationTypePerc1.get())/float(e_hydrationPerc.get()))
    g_hydrationType2 = g_hydration*(float(e_hydrationTypePerc2.get())/float(e_hydrationPerc.get()))
    if g_fat == 0:
        g_fatType1 = 0
        g_fatType2 = 0
    else:
        g_fatType1 = g_fat*(float(e_fatTypePerc1.get())/float(e_fatPerc.get()))
        g_fatType2 = g_fat*(float(e_fatTypePerc2.get())/float(e_fatPerc.get()))
    e_flourTypeWeight1.delete(0, END)
    e_flourTypeWeight1.insert(0, round(g_flourTypeWeight1, 0))
    e_flourTypeWeight2.delete(0, END)
    e_flourTypeWeight2.insert(0, round(g_flourTypeWeight2, 0))
    e_flourTypeWeight3.delete(0, END)
    e_flourTypeWeight3.insert(0, round(g_flourTypeWeight3, 0))
    e_hydrationTypeWeight1.delete(0, END)
    e_hydrationTypeWeight1.insert(0, round(g_hydrationType1, 0))
    e_hydrationTypeWeight2.delete(0, END)
    e_hydrationTypeWeight2.insert(0, round(g_hydrationType2, 0))
    e_fatTypeWeight1.delete(0, END)
    e_fatTypeWeight1.insert(0, round(g_fatType1, 0))
    e_fatTypeWeight2.delete(0, END)
    e_fatTypeWeight2.insert(0, round(g_fatType2, 0))

def calculatePerc():
    return;
    
def showCard():
    calculateRecipe()
    exec(open("generateRecipeCard.py").read())
    
def exportRecipeCard():
    return;    
    
def saveRecipe():
    return;

def saveRecipeAs():
    return;    
    
def deleteRecipe():
    return;        
