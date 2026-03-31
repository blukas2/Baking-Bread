# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:35:20 2020

@author: Balázs
"""

# Lists    
flourTypeList = ['none', 'BL55 buzafinomliszt', 'BL80 kenyerliszt', 'rozsliszt', 
                 'TK buzaliszt', 'TK rozsliszt', 'zabliszt']

hydrationTypeList = ['none', 'buzasor', 'gyumolcsle', 'joghurt', 'kokusztej', 'tej',
                     'viz', 'zabtej']

fatTypeList = ['none', 'kokuszzsir', 'oliva olaj', 'tojas', 'vaj']

sugarTypeList = ['none', 'barnacukor', 'kristalycukor', 'mez', 'nadcukor']

# read dataset
breadDataset = pd.read_csv("breadDataset.csv")
#global breadDataset
#breadDataset = breadDataset2

# BUTTONS
# Recipe calculator    
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

# Recipe card    
def showCard():
    calculateRecipe()
    exec(open("generateRecipeCard.py").read())
    
def exportRecipeCard():
    return;    


# recipe book
def breadSelect(evt):
    selectedData = breadDataset[breadDataset['breadName']==lb_recipes.get(lb_recipes.curselection())].reset_index(drop = True)
    flourType1.set(selectedData['flourType1'][0])
    flourType2.set(selectedData['flourType2'][0])
    flourType3.set(selectedData['flourType3'][0])
    e_flourTypePerc1.delete(0, END)
    e_flourTypePerc1.insert(0, selectedData['e_flourTypePerc1'][0])
    e_flourTypePerc2.delete(0, END)
    e_flourTypePerc2.insert(0, selectedData['e_flourTypePerc2'][0])
    e_flourTypePerc3.delete(0, END)
    e_flourTypePerc3.insert(0, selectedData['e_flourTypePerc3'][0])
    e_hydrationPerc.delete(0, END)
    e_hydrationPerc.insert(0, selectedData['e_hydrationPerc'][0])
    hydrationType1.set(selectedData['hydrationType1'][0])
    hydrationType2.set(selectedData['hydrationType2'][0])
    e_hydrationTypePerc1.delete(0, END)
    e_hydrationTypePerc1.insert(0, selectedData['e_hydrationTypePerc1'][0])
    e_hydrationTypePerc2.delete(0, END)
    e_hydrationTypePerc2.insert(0, selectedData['e_hydrationTypePerc2'][0])
    e_fatPerc.delete(0, END)
    e_fatPerc.insert(0, selectedData['e_fatPerc'][0])
    fatType1.set(selectedData['fatType1'][0])
    fatType2.set(selectedData['fatType2'][0])    
    e_fatTypePerc1.delete(0, END)
    e_fatTypePerc1.insert(0, selectedData['e_fatTypePerc1'][0])
    e_fatTypePerc2.delete(0, END)
    e_fatTypePerc2.insert(0, selectedData['e_fatTypePerc2'][0])
    e_saltPerc.delete(0, END)
    e_saltPerc.insert(0, selectedData['e_saltPerc'][0])    
    sugarType.set(selectedData['sugarType'][0])
    e_sugarPerc.delete(0, END)
    e_sugarPerc.insert(0, selectedData['e_sugarPerc'][0])
    e_leavenShare.delete(0, END)
    e_leavenShare.insert(0, selectedData['e_leavenShare'][0])
    e_leavenHydration.delete(0, END)
    e_leavenHydration.insert(0, selectedData['e_leavenHydration'][0])
    flourTypeLeaven1.set(selectedData['flourTypeLeaven1'][0])
    flourTypeLeaven2.set(selectedData['flourTypeLeaven2'][0])
    e_flourTypeLeaven1.delete(0, END)
    e_flourTypeLeaven1.insert(0, selectedData['e_flourTypeLeaven1'][0])
    e_flourTypeLeaven2.delete(0, END)
    e_flourTypeLeaven2.insert(0, selectedData['e_flourTypeLeaven2'][0])
    e_loafWeight.delete(0, END)
    e_loafWeight.insert(0, selectedData['e_loafWeight'][0])
    txt_comments.delete(1.0, END)
    txt_comments.insert(INSERT, selectedData['txt_comments'][0])
    calculateRecipe()    

    
    
    
#    tlvl_test = Toplevel()
#    tlvl_test.title(lb_recipes.get(lb_recipes.curselection()))

    
def saveRecipe():
    try:
        recipeName = lb_recipes.get(lb_recipes.curselection())
    except:
        tlvl_recipeToSelect = Toplevel()
        tlvl_recipeToSelect.title('Save recipe')
        lbl_delRec_toSelect_descr = tk.Label(tlvl_recipeToSelect, text = "No recipe selected, choose one!")
        lbl_delRec_toSelect_descr.config(anchor = CENTER)
        lbl_delRec_toSelect_descr.pack(pady=10)
        btn_delRec_toSelect_ok = tk.Button(tlvl_recipeToSelect, text="OK", width=8, command=tlvl_recipeToSelect.destroy)
        btn_delRec_toSelect_ok.pack(pady = 10)
    else:
        global tlvl_saveRecipe
        tlvl_saveRecipe = Toplevel()
        tlvl_saveRecipe.title('Save recipe')
        lbl_savRec_descr = tk.Label(tlvl_saveRecipe, text = "WARNING! Are you sure you want to overwrite this recipe?")
        lbl_savRec_descr.config(anchor = CENTER, font=titleFont)
        lbl_savRec_descr.pack(pady=10)
        lbl_savRec_name = tk.Label(tlvl_saveRecipe, text = recipeName)
        lbl_savRec_name.config(anchor = CENTER)
        lbl_savRec_name.pack()
        frm_savRec_buttons = Frame(tlvl_saveRecipe)
        frm_savRec_buttons.pack()
        btn_savRec_yes = tk.Button(frm_savRec_buttons, text="Yes", width=8, command=saveRecipeYes)
        btn_savRec_yes.pack(side=LEFT, padx=10, pady = 10)
        btn_savRec_no = tk.Button(frm_savRec_buttons, text="No", width=8, command=tlvl_saveRecipe.destroy)
        btn_savRec_no.pack(side = RIGHT, padx=10, pady = 10)
    
def saveRecipeYes():
    recipeName = lb_recipes.get(lb_recipes.curselection())
    dataCollect = {'breadName': recipeName, 
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
            'e_fatTypePerc1':float(e_fatTypePerc1.get()),
            'e_fatTypePerc2':float(e_fatTypePerc2.get()),
            'e_saltPerc':float(e_saltPerc.get()),
            'sugarType':sugarType.get(),
            'e_sugarPerc':float(e_sugarPerc.get()),
            'e_leavenShare':float(e_leavenShare.get()),
            'e_leavenHydration':float(e_leavenHydration.get()),
            'flourTypeLeaven1':flourTypeLeaven1.get(),
            'flourTypeLeaven2':flourTypeLeaven2.get(),
            'e_flourTypeLeaven1':float(e_flourTypeLeaven1.get()),
            'e_flourTypeLeaven2':float(e_flourTypeLeaven2.get()),
            'e_loafWeight':float(e_loafWeight.get()),
            'txt_comments':txt_comments.get(1.0, END)}    
    global breadDataset   
    breadDataset = breadDataset[breadDataset['breadName']!=recipeName]
    breadDataset = breadDataset.append(dataCollect, ignore_index = True)
    breadDataset = breadDataset.sort_values(by = ['breadName'], ignore_index = True, ascending = False)
    lb_recipes.delete(0, tk.END)
    for i in breadDataset['breadName'].tolist():
        lb_recipes.insert(0, i)       
    tlvl_saveRecipe.destroy()
    


def saveRecipeAs():
    global tlvl_nameYourBread
    tlvl_nameYourBread = Toplevel()
    tlvl_nameYourBread.title('Name your bread!')
    lbl_nyb_descr = tk.Label(tlvl_nameYourBread, text = "Enter the name of your new recipe!")
    lbl_nyb_descr.config(anchor = CENTER, font=titleFont)
    lbl_nyb_descr.pack(pady=10)
    global nyb_breadName
    nyb_breadName=StringVar()
    e_nyb_breadName = Entry(tlvl_nameYourBread, width = 20, borderwidth = 5, textvariable=nyb_breadName)
    e_nyb_breadName.pack()
    frm_nyb_buttons = Frame(tlvl_nameYourBread)
    frm_nyb_buttons.pack()
    btn_nyb_ok = tk.Button(frm_nyb_buttons, text="OK", width=8, command=saveRecipeAsOk)
    btn_nyb_ok.pack(side=LEFT, padx=10, pady = 10)
    btn_nyb_cancel = tk.Button(frm_nyb_buttons, text="Cancel", width=8, command=tlvl_nameYourBread.destroy)
    btn_nyb_cancel.pack(side = RIGHT, padx=10, pady = 10)
    
    
    
def saveRecipeAsOk():
   dataCollect = {'breadName': nyb_breadName.get(), 
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
           'e_fatTypePerc1':float(e_fatTypePerc1.get()),
           'e_fatTypePerc2':float(e_fatTypePerc2.get()),
           'e_saltPerc':float(e_saltPerc.get()),
           'sugarType':sugarType.get(),
           'e_sugarPerc':float(e_sugarPerc.get()),
           'e_leavenShare':float(e_leavenShare.get()),
           'e_leavenHydration':float(e_leavenHydration.get()),
           'flourTypeLeaven1':flourTypeLeaven1.get(),
           'flourTypeLeaven2':flourTypeLeaven2.get(),
           'e_flourTypeLeaven1':float(e_flourTypeLeaven1.get()),
           'e_flourTypeLeaven2':float(e_flourTypeLeaven2.get()),
           'e_loafWeight':float(e_loafWeight.get()),
           'txt_comments':txt_comments.get(1.0, END)}
   global breadDataset
   breadDataset = breadDataset.append(dataCollect, ignore_index = True)
   breadDataset = breadDataset.sort_values(by = ['breadName'], ignore_index = True, ascending = False)
   lb_recipes.delete(0, tk.END)
   for i in breadDataset['breadName'].tolist():
       lb_recipes.insert(0, i)       
   tlvl_nameYourBread.destroy()
   
    

    
def deleteRecipe():
    try:
        recipeName = lb_recipes.get(lb_recipes.curselection())
    except:
        tlvl_deleteRecipe_toSelect = Toplevel()
        tlvl_deleteRecipe_toSelect.title('Delete recipe')
        lbl_delRec_toSelect_descr = tk.Label(tlvl_deleteRecipe_toSelect, text = "No recipe selected, choose one!")
        lbl_delRec_toSelect_descr.config(anchor = CENTER)
        lbl_delRec_toSelect_descr.pack(pady=10)
        btn_delRec_toSelect_ok = tk.Button(tlvl_deleteRecipe_toSelect, text="OK", width=8, command=tlvl_deleteRecipe_toSelect.destroy)
        btn_delRec_toSelect_ok.pack(pady = 10)
    else:
        global tlvl_deleteRecipe
        tlvl_deleteRecipe = Toplevel()
        tlvl_deleteRecipe.title('Delete recipe')
        lbl_delRec_descr = tk.Label(tlvl_deleteRecipe, text = "WARNING! Are you sure you want to delete this recipe?")
        lbl_delRec_descr.config(anchor = CENTER, font=titleFont)
        lbl_delRec_descr.pack(pady=10)
        lbl_delRec_name = tk.Label(tlvl_deleteRecipe, text = recipeName)
        lbl_delRec_name.config(anchor = CENTER)
        lbl_delRec_name.pack()
        frm_delRec_buttons = Frame(tlvl_deleteRecipe)
        frm_delRec_buttons.pack()
        btn_delRec_yes = tk.Button(frm_delRec_buttons, text="Yes", width=8, command=deleteRecipeYes)
        btn_delRec_yes.pack(side=LEFT, padx=10, pady = 10)
        btn_delRec_no = tk.Button(frm_delRec_buttons, text="No", width=8, command=tlvl_deleteRecipe.destroy)
        btn_delRec_no.pack(side = RIGHT, padx=10, pady = 10)



def deleteRecipeYes():
    global breadDataset
    breadDataset = breadDataset[breadDataset['breadName']!=lb_recipes.get(lb_recipes.curselection())]
    breadDataset = breadDataset.sort_values(by = ['breadName'], ignore_index = True, ascending = False)
    lb_recipes.delete(0, tk.END)
    for i in breadDataset['breadName'].tolist():
        lb_recipes.insert(0, i)       
    tlvl_deleteRecipe.destroy()

def renameRecipe():
    try:
        recipeName = lb_recipes.get(lb_recipes.curselection())
    except:
        tlvl_recipeToSelect = Toplevel()
        tlvl_recipeToSelect.title('Rename recipe')
        lbl_delRec_toSelect_descr = tk.Label(tlvl_recipeToSelect, text = "No recipe selected, choose one!")
        lbl_delRec_toSelect_descr.config(anchor = CENTER)
        lbl_delRec_toSelect_descr.pack(pady=10)
        btn_delRec_toSelect_ok = tk.Button(tlvl_recipeToSelect, text="OK", width=8, command=tlvl_recipeToSelect.destroy)
        btn_delRec_toSelect_ok.pack(pady = 10)
    else:
        global tlvl_renameYourBread
        tlvl_renameYourBread = Toplevel()
        tlvl_renameYourBread.title('Rename your bread!')
        lbl_rnyb_descr = tk.Label(tlvl_renameYourBread, text = ''.join(["You will rename ", recipeName, " to:"]))
        lbl_rnyb_descr.config(anchor = CENTER, font=titleFont)
        lbl_rnyb_descr.pack(pady=10)
        global rnyb_breadName
        rnyb_breadName=StringVar()
        e_rnyb_breadName = Entry(tlvl_renameYourBread, width = 20, borderwidth = 5, textvariable=rnyb_breadName)
        e_rnyb_breadName.pack()
        frm_rnyb_buttons = Frame(tlvl_renameYourBread)
        frm_rnyb_buttons.pack()
        btn_rnyb_ok = tk.Button(frm_rnyb_buttons, text="OK", width=8, command=renameRecipeOk)
        btn_rnyb_ok.pack(side=LEFT, padx=10, pady = 10)
        btn_rnyb_cancel = tk.Button(frm_rnyb_buttons, text="Cancel", width=8, command=tlvl_renameYourBread.destroy)
        btn_rnyb_cancel.pack(side = RIGHT, padx=10, pady = 10)
        
def renameRecipeOk():
    global breadDataset
    if(rnyb_breadName.get() == "" or rnyb_breadName.get() == " "):
        tlvl_invalidName = Toplevel()
        tlvl_invalidName.title('Invalid name!')
        lbl_ivName_descr = tk.Label(tlvl_invalidName, text = "The name you entered is invalid. Try another one!")
        lbl_ivName_descr.config(anchor = CENTER)
        lbl_ivName_descr.pack(pady=10)
        btn_ivName_ok = tk.Button(tlvl_invalidName, text="OK", width=8, command=tlvl_invalidName.destroy)
        btn_ivName_ok.pack(pady = 10)
    elif(rnyb_breadName.get() in breadDataset['breadName'].tolist()):
        tlvl_invalidName = Toplevel()
        tlvl_invalidName.title('Invalid name!')
        lbl_ivName_descr = tk.Label(tlvl_invalidName, text = "The name you entered already exists. Try another one!")
        lbl_ivName_descr.config(anchor = CENTER)
        lbl_ivName_descr.pack(pady=10)
        btn_ivName_ok = tk.Button(tlvl_invalidName, text="OK", width=8, command=tlvl_invalidName.destroy)
        btn_ivName_ok.pack(pady = 10)
    else:
        originalName = lb_recipes.get(lb_recipes.curselection())
        renamedEntry = breadDataset[breadDataset['breadName']==originalName].reset_index(drop = True)
        renamedEntry['breadName'][0] = rnyb_breadName.get()
        breadDataset = breadDataset[breadDataset['breadName']!=originalName]
#        breadDataset = pd.merge(breadDataset, renamedEntry, how = 'outer', on = ['breadName'])
        breadDataset = pd.concat([breadDataset, renamedEntry])
        breadDataset = breadDataset.sort_values(by = ['breadName'], ignore_index = True, ascending = False)
        lb_recipes.delete(0, tk.END)
        for i in breadDataset['breadName'].tolist():
            lb_recipes.insert(0, i)       
        tlvl_renameYourBread.destroy()        
    

    
def updateDataset():
    global breadDataset
    shutil.copy2(''.join([os.getcwd(), '/dataset_saves/old2_breadDataset.csv']), ''.join([os.getcwd(), '/dataset_saves/old3_breadDataset.csv']))    
    shutil.copy2(''.join([os.getcwd(), '/dataset_saves/old1_breadDataset.csv']), ''.join([os.getcwd(), '/dataset_saves/old2_breadDataset.csv']))
    shutil.copy2(''.join([os.getcwd(), '/breadDataset.csv']), ''.join([os.getcwd(), '/dataset_saves/old1_breadDataset.csv']))
    breadDataset.to_csv("breadDataset.csv", index = FALSE)
    tlvl_datasetUpdated = Toplevel()
    tlvl_datasetUpdated.title('Recipe Book Updated!')
    lbl_dsUpdate_descr = tk.Label(tlvl_datasetUpdated, text = "Changes successfully updated in the recipe book!")
    lbl_dsUpdate_descr.config(anchor = CENTER)
    lbl_dsUpdate_descr.pack(pady=10)
    btn_dsUpdate_ok = tk.Button(tlvl_datasetUpdated, text="Great!", width=8, command=tlvl_datasetUpdated.destroy)
    btn_dsUpdate_ok.pack(pady = 10)    
    
