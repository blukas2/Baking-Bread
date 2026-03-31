# -*- coding: utf-8 -*-

import tkinter as tk


from tkinter import *
from tkinter import ttk
root = Tk()
ttk.Button(root, text="Hello World").grid()
root.mainloop()



window = tk.Tk()    

frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

frame_b = tk.Frame()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Swap the order of `frame_a` and `frame_b`
frame_b.pack()
frame_a.pack()

window.mainloop()

window = tk.Tk()
label = tk.Label(text="this is the label")
label.pack()
button = tk.Button(text = "Click me!", width = 10, height = 3)
button.pack()
window.mainloop()


breadDataset = {'breadName':['Alapkenyer'], 
           'flourType1':['BL80 kenyerliszt'],
           'flourType2':['TK buzaliszt'],
           'flourType3':['none'],
           'e_flourTypePerc1':[75],
           'e_flourTypePerc2':[25],
           'e_flourTypePerc3':[0],
           'e_hydrationPerc':[80],
           'hydrationType1':['viz'],
           'hydrationType2':['none'],
           'e_hydrationTypePerc1':[80],
           'e_hydrationTypePerc2':[0],
           'e_fatPerc':[0],
           'fatType1':['none'],
           'fatType2':['none'],
           'e_fatTypePerc1':[0],
           'e_fatTypePerc2':[0],
           'e_saltPerc':[2.2],
           'sugarType':['none'],
           'e_sugarPerc':[0],
           'e_leavenShare':[20],
           'e_leavenHydration':[80],
           'e_poolishShare':[0],
           'e_poolishHydration':[0],
           'e_tangzhongShare':[0],
           'e_loafWeight':[500],

           'flourTypeLeaven1':['TK buzaliszt'],
           'flourTypeLeaven2':['none'],
           'e_flourTypeLeaven1':[100],
           'e_flourTypeLeaven2':[0],
           'flourTypePoolish1':['none'],
           'flourTypePoolish2':['none'],
           'e_flourTypePoolish1':[0],
           'e_flourTypePoolish2':[0],
           'e_prefrmt_poolish_leavenShare':[0],
           'e_prefrmt_poolish_leavenHydration':[0],
           'flourTypeTangzhong':['none'],
           
           'txt_comments':[' ']
    }

breadDataset = pd.DataFrame(breadDataset)

breadDataset.to_csv("breadDataset.csv", index = FALSE)

#import csv

breadDataset = pd.read_csv("breadDataset.csv")

print(breadDataset['breadName'][0])


testDataframe = {'name':['John'],
               'job_title':['taxi driver']}

testDataframe = pd.DataFrame(testDataframe)

testDataframe = testDataframe.append({
    'name':'Samuel',
    'job_title':'caretaker'
    }, ignore_index = True)


print(testDataframe['name'].tolist())


def saveRecipeAsOk():
   dataCollect = {'breadName': e_nyb_breadName.get(), 
           'flourType1':flourType1.get(),
           'flourType2':flourType2.get(),
           'flourType3':flourType3.get(),
           'e_flourTypePerc1':float(e_flourTypePerc1.get()),
           'e_flourTypePerc2':float(e_flourTypePerc2.get()),
           'e_flourTypePerc3':float(e_flourTypePerc3.get()),
           'e_hydrationPerc':float(e_hydrationPerc.get()),
           'hydrationType1':hydrationType1.get(),
           'hydrationType2':hydrationType2.get(),
           'e_hydrationTypePerc1':float(e_hydrationTypePerc1.get()),
           'e_hydrationTypePerc2':float(e_hydrationTypePerc2.get()),
           'e_fatPerc':float(e_fatPerc.get()),
           'fatType1':fatType1.get(),
           'fatType2':fatType2.get(),
           'e_fatTypePerc1':float(fatTypePerc1.get()),
           'e_fatTypePerc2':float(fatTypePerc2.get()),
           'e_saltPerc':float(e_saltPerc1.get()),
           'sugarType':sugarType.get(),
           'e_sugarPerc':float(e_sugarPerc.get()),
           'e_leavenShare':float(e_leavenShare.get()),
           'e_leavenHydration':float(e_leavenHydration.get()),
           'flourTypeLeaven1':flourTypeLeaven1.get(),
           'flourTypeLeaven2':flourTypeLeaven2.get(),
           'e_flourTypeLeaven1':float(e_flourTypeLeaven1.get()),
           'e_flourTypeLeaven2':float(e_flourTypeLeaven2.get()),
           'e_loafWeight':float(e_loafWeight.get()),
           'txt_comments':txt_comments.get(1.0, END)
   breadDataset = breadDataset.append(dataCollect, ignore_index = True)
   breadDataset = breadDataset.sort_values(by = ['breadName'])
   global lb_recipes
   lb_recipes.Items.Clear()
   for i in [breadDataset['breadName'].tolist()]:
       lb_recipes.insert(0, i)     
    }
    
    
    return;  



def breadSelect(evt):
    selectedData = breadDataset[breadDataset['breadName']==lb_recipes.get(lb_recipes.curselection())]
    flourType1.set(breadDataset['flourType1'][0])
    flourType2.set(breadDataset['flourType2'][0])
    flourType3.set(breadDataset['flourType3'][0])
    e_flourTypePerc1.delete(0, END)
    e_flourTypePerc1.insert(0, breadDataset['e_flourTypePerc1'][0])
    e_flourTypePerc2.delete(0, END)
    e_flourTypePerc2.insert(0, breadDataset['e_flourTypePerc2'][0])
    e_flourTypePerc3.delete(0, END)
    e_flourTypePerc3.insert(0, breadDataset['e_flourTypePerc3'][0])
    e_hydrationPerc.delete(0, END)
    e_hydrationPerc.insert(0, breadDataset['e_hydrationPerc'][0])
    hydrationType1.set(breadDataset['hydrationType1'][0])
    hydrationType2.set(breadDataset['hydrationType2'][0])
    e_hydrationTypePerc1.delete(0, END)
    e_hydrationTypePerc1.insert(0, breadDataset['e_hydrationTypePerc1'][0])
    e_hydrationTypePerc2.delete(0, END)
    e_hydrationTypePerc2.insert(0, breadDataset['e_hydrationTypePerc2'][0])
    e_fatPerc.delete(0, END)
    e_fatPerc.insert(0, breadDataset['e_fatPerc'][0])
    fatType1.set(breadDataset['fatType1'][0])
    fatType2.set(breadDataset['fatType2'][0])    
    e_fatTypePerc1.delete(0, END)
    e_fatTypePerc1.insert(0, breadDataset['e_fatTypePerc1'][0])
    e_fatTypePerc2.delete(0, END)
    e_fatTypePerc2.insert(0, breadDataset['e_fatTypePerc2'][0])
    e_saltPerc.delete(0, END)
    e_saltPerc.insert(0, breadDataset['e_saltPerc'][0])    
    sugarType.set(breadDataset['sugarType'][0])
    e_sugarPerc.delete(0, END)
    e_sugarPerc.insert(0, breadDataset['e_sugarPerc'][0])
    e_leavenShare.delete(0, END)
    e_leavenShare.insert(0, breadDataset['e_leavenShare'][0])
    e_leavenHydration.delete(0, END)
    e_leavenHydration.insert(0, breadDataset['e_leavenHydration'][0])
    flourTypeLeaven1.set(breadDataset['flourTypeLeaven1'][0])
    flourTypeLeaven2.set(breadDataset['flourTypeLeaven2'][0])
    e_flourTypeLeaven1.delete(0, END)
    e_flourTypeLeaven1.insert(0, breadDataset['e_flourTypeLeaven1'][0])
    e_flourTypeLeaven2.delete(0, END)
    e_flourTypeLeaven2.insert(0, breadDataset['e_flourTypeLeaven2'][0])
    e_loafWeight.delete(0, END)
    e_loafWeight.insert(0, breadDataset['e_loafWeight'][0])
    txt_comments.delete(1.0, END)
    txt_comments.insert(INSERT, breadDataset['txt_comments'][0])
    calculateRecipe()

def deleteRecipe():
    if(math.isnan(lb_recipes.get(lb_recipes.curselection()))==False):
        global tlvl_deleteRecipe
        tlvl_deleteRecipe = Toplevel()
        tlvl_deleteRecipe.title('Delete recipe')
        lbl_delRec_descr = tk.Label(tlvl_deleteRecipe, text = "WARNING! Are you sure you want to delete this recipe?")
        lbl_delRec_descr.config(anchor = CENTER, font=titleFont)
        lbl_delRec_descr.pack(pady=10)
        frm_delRec_buttons = Frame(tlvl_deleteRecipe)
        frm_delRec_buttons.pack()
        btn_delRec_yes = tk.Button(frm_delRec_buttons, text="Yes", width=8, command=deleteRecipeYes)
        btn_delRec_yes.pack(side=LEFT, padx=10, pady = 10)
        btn_delRec_no = tk.Button(frm_delRec_buttons, text="No", width=8, command=tlvl_deleteRecipe.destroy)
        btn_delRec_no.pack(side = RIGHT, padx=10, pady = 10)
    else:
        global tlvl_deleteRecipe_toSelect
        tlvl_deleteRecipe_toSelect = Toplevel()
        tlvl_deleteRecipe_toSelect.title('Delete recipe')
        lbl_delRec_toSelect_descr = tk.Label(tlvl_deleteRecipe_toSelect, text = "No recipe selected, choose one!")
        lbl_delRec_toSelect_descr.config(anchor = CENTER)
        lbl_delRec_toSelect_descr.pack(pady=10)
        btn_delRec_toSelect_ok = tk.Button(tlvl_deleteRecipe_toSelect, text="Yes", width=8, command=tlvl_deleteRecipe_toSelect.destroy)
        btn_delRec_toSelect_ok.pack(pady = 10)


print(breadDataset)

breadDataset3 = breadDataset[breadDataset['breadName']=="Alapkenyer"].reset_index(drop = True)
breadDataset3['breadName'][0]="jokenyer"

print(breadDataset3['flourType1'][0])

print(breadDataset3.head(1))


print('Alapkenyer' in breadDataset['breadName'].tolist())

print(os.getcwd())



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