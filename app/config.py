# -*- coding: utf-8 -*-

FLOUR_TYPES = [
    'none', 'BL55 buzafinomliszt', 'BL80 kenyerliszt', 'durumliszt',
    'rozsliszt', 'TK buzaliszt', 'TK rozsliszt', 'zabliszt'
]

HYDRATION_TYPES = [
    'none', 'buzasor', 'gyumolcsle', 'joghurt', 'kokusztej',
    'tej', 'viz', 'zabtej'
]

FAT_TYPES = ['none', 'kokuszzsir', 'oliva olaj', 'tojas', 'vaj']

SUGAR_TYPES = ['none', 'barnacukor', 'kristalycukor', 'mez', 'nadcukor']

TITLE_FONT = "Arial 10 bold"
ENTRY_WIDTH = 10
ENTRY_BORDER = 5
DROPDOWN_WIDTH = 16

DEFAULT_VALUES = {
    'bread_name': '',
    'flour_type_1': 'BL80 kenyerliszt',
    'flour_type_2': 'TK buzaliszt',
    'flour_type_3': 'none',
    'flour_percentage_1': 75.0,
    'flour_percentage_2': 25.0,
    'flour_percentage_3': 0.0,
    'hydration_percentage': 80.0,
    'hydration_type_1': 'viz',
    'hydration_type_2': 'none',
    'hydration_type_percentage_1': 80.0,
    'hydration_type_percentage_2': 0.0,
    'fat_percentage': 0.0,
    'fat_type_1': 'none',
    'fat_type_2': 'none',
    'fat_type_percentage_1': 0.0,
    'fat_type_percentage_2': 0.0,
    'salt_percentage': 2.2,
    'sugar_type': 'none',
    'sugar_percentage': 0.0,
    'leaven_share': 20.0,
    'leaven_hydration': 80.0,
    'poolish_share': 0.0,
    'poolish_hydration': 0.0,
    'tangzhong_share': 0.0,
    'loaf_weight': 500.0,
    'leaven_flour_type_1': 'rozsliszt',
    'leaven_flour_type_2': 'none',
    'leaven_flour_percentage_1': 100.0,
    'leaven_flour_percentage_2': 0.0,
    'poolish_flour_type_1': 'none',
    'poolish_flour_type_2': 'none',
    'poolish_flour_percentage_1': 0.0,
    'poolish_flour_percentage_2': 0.0,
    'poolish_leaven_share': 0.0,
    'poolish_leaven_hydration': 0.0,
    'tangzhong_flour_type': 'none',
    'comments': '',
}

CSV_COLUMN_MAP = {
    'breadName': 'bread_name',
    'flourType1': 'flour_type_1',
    'flourType2': 'flour_type_2',
    'flourType3': 'flour_type_3',
    'e_flourTypePerc1': 'flour_percentage_1',
    'e_flourTypePerc2': 'flour_percentage_2',
    'e_flourTypePerc3': 'flour_percentage_3',
    'e_hydrationPerc': 'hydration_percentage',
    'hydrationType1': 'hydration_type_1',
    'hydrationType2': 'hydration_type_2',
    'e_hydrationTypePerc1': 'hydration_type_percentage_1',
    'e_hydrationTypePerc2': 'hydration_type_percentage_2',
    'e_fatPerc': 'fat_percentage',
    'fatType1': 'fat_type_1',
    'fatType2': 'fat_type_2',
    'e_fatTypePerc1': 'fat_type_percentage_1',
    'e_fatTypePerc2': 'fat_type_percentage_2',
    'e_saltPerc': 'salt_percentage',
    'sugarType': 'sugar_type',
    'e_sugarPerc': 'sugar_percentage',
    'e_leavenShare': 'leaven_share',
    'e_leavenHydration': 'leaven_hydration',
    'e_poolishShare': 'poolish_share',
    'e_poolishHydration': 'poolish_hydration',
    'e_tangzhongShare': 'tangzhong_share',
    'e_loafWeight': 'loaf_weight',
    'flourTypeLeaven1': 'leaven_flour_type_1',
    'flourTypeLeaven2': 'leaven_flour_type_2',
    'e_flourTypeLeaven1': 'leaven_flour_percentage_1',
    'e_flourTypeLeaven2': 'leaven_flour_percentage_2',
    'flourTypePoolish1': 'poolish_flour_type_1',
    'flourTypePoolish2': 'poolish_flour_type_2',
    'e_flourTypePoolish1': 'poolish_flour_percentage_1',
    'e_flourTypePoolish2': 'poolish_flour_percentage_2',
    'e_prefrmt_poolish_leavenShare': 'poolish_leaven_share',
    'e_prefrmt_poolish_leavenHydration': 'poolish_leaven_hydration',
    'flourTypeTangzhong': 'tangzhong_flour_type',
    'txt_comments': 'comments',
}
