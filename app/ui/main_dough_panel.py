# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import END

from config import (
    FLOUR_TYPES, HYDRATION_TYPES, FAT_TYPES, SUGAR_TYPES, TITLE_FONT
)
from ui.widget_helpers import (
    create_ingredient_row, create_labeled_row, create_entry,
    add_separator, update_entry
)


class MainDoughPanel(tk.Frame):

    def __init__(self, parent, on_calculate_all, on_calculate_weights, on_show_card):
        super().__init__(parent)
        self._string_vars = {}
        self._entries = {}
        self._current_row = 0
        self._build_header(on_show_card)
        self._build_flour_section()
        self._build_hydration_section()
        self._build_fat_section()
        self._build_salt_section()
        self._build_sugar_section()
        self._build_leaven_section()
        self._build_poolish_section()
        self._build_tangzhong_section()
        self._build_loaf_weight_section()
        self._build_buttons(on_calculate_all, on_calculate_weights)

    def _build_header(self, on_show_card):
        btn = tk.Button(self, text="Show card", command=on_show_card)
        btn.grid(row=0, column=0)
        lbl_perc = tk.Label(self, text="Baker's %", font=TITLE_FONT, anchor=tk.CENTER)
        lbl_perc.grid(row=0, column=1)
        lbl_weight = tk.Label(self, text="Weight (g)", font=TITLE_FONT, anchor=tk.CENTER)
        lbl_weight.grid(row=0, column=2)
        self._current_row = 1
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _add_ingredient_row(self, key_prefix, options):
        var = tk.StringVar()
        self._string_vars[key_prefix + '_type'] = var
        _, perc, weight = create_ingredient_row(self, var, options, self._current_row, 0)
        self._entries[key_prefix + '_percentage'] = perc
        self._entries[key_prefix + '_weight'] = weight
        self._current_row += 1

    def _add_labeled_row(self, label_text, key_prefix):
        _, perc, weight = create_labeled_row(self, label_text, self._current_row, 0)
        self._entries[key_prefix + '_percentage'] = perc
        self._entries[key_prefix + '_weight'] = weight
        self._current_row += 1

    def _add_labeled_entry(self, label_text, key):
        label = tk.Label(self, text=label_text)
        label.grid(row=self._current_row, column=0)
        entry = create_entry(self)
        entry.grid(row=self._current_row, column=1)
        self._entries[key] = entry
        self._current_row += 1

    def _build_flour_section(self):
        for i in range(1, 4):
            self._add_ingredient_row(f'flour_{i}', FLOUR_TYPES)
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_hydration_section(self):
        self._add_labeled_row("Hydration", 'hydration')
        for i in range(1, 3):
            self._add_ingredient_row(f'hydration_type_{i}', HYDRATION_TYPES)
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_fat_section(self):
        self._add_labeled_row("Fat", 'fat')
        for i in range(1, 3):
            self._add_ingredient_row(f'fat_type_{i}', FAT_TYPES)
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_salt_section(self):
        self._add_labeled_row("Salt", 'salt')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_sugar_section(self):
        self._add_ingredient_row('sugar', SUGAR_TYPES)
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_leaven_section(self):
        self._add_labeled_row("Leaven", 'leaven_share')
        self._add_labeled_entry("Leaven hydration", 'leaven_hydration')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_poolish_section(self):
        self._add_labeled_row("Poolish", 'poolish_share')
        self._add_labeled_entry("Poolish hydration", 'poolish_hydration')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_tangzhong_section(self):
        self._add_labeled_row("Tangzhong", 'tangzhong_share')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_loaf_weight_section(self):
        self._add_labeled_entry("Loaf weight (g)", 'loaf_weight')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_buttons(self, on_calculate_all, on_calculate_weights):
        btn_all = tk.Button(self, text="CALCULATE ALL!", command=on_calculate_all)
        btn_all.grid(row=self._current_row, column=0)
        btn_weight = tk.Button(self, text="Calculate weight", command=on_calculate_weights)
        btn_weight.grid(row=self._current_row, column=1)
        btn_perc = tk.Button(self, text="Calculate %s", state=tk.DISABLED)
        btn_perc.grid(row=self._current_row, column=2)

    def get_recipe_fields(self):
        return {
            'flour_type_1': self._string_vars['flour_1_type'].get(),
            'flour_type_2': self._string_vars['flour_2_type'].get(),
            'flour_type_3': self._string_vars['flour_3_type'].get(),
            'flour_percentage_1': self._get_float('flour_1_percentage'),
            'flour_percentage_2': self._get_float('flour_2_percentage'),
            'flour_percentage_3': self._get_float('flour_3_percentage'),
            'hydration_percentage': self._get_float('hydration_percentage'),
            'hydration_type_1': self._string_vars['hydration_type_1_type'].get(),
            'hydration_type_2': self._string_vars['hydration_type_2_type'].get(),
            'hydration_type_percentage_1': self._get_float('hydration_type_1_percentage'),
            'hydration_type_percentage_2': self._get_float('hydration_type_2_percentage'),
            'fat_percentage': self._get_float('fat_percentage'),
            'fat_type_1': self._string_vars['fat_type_1_type'].get(),
            'fat_type_2': self._string_vars['fat_type_2_type'].get(),
            'fat_type_percentage_1': self._get_float('fat_type_1_percentage'),
            'fat_type_percentage_2': self._get_float('fat_type_2_percentage'),
            'salt_percentage': self._get_float('salt_percentage'),
            'sugar_type': self._string_vars['sugar_type'].get(),
            'sugar_percentage': self._get_float('sugar_percentage'),
            'leaven_share': self._get_float('leaven_share_percentage'),
            'leaven_hydration': self._get_float('leaven_hydration'),
            'poolish_share': self._get_float('poolish_share_percentage'),
            'poolish_hydration': self._get_float('poolish_hydration'),
            'tangzhong_share': self._get_float('tangzhong_share_percentage'),
            'loaf_weight': self._get_float('loaf_weight'),
        }

    def _get_float(self, key):
        value = self._entries[key].get()
        if not value or value.strip() == '':
            return 0.0
        return float(value)

    def set_recipe(self, recipe):
        self._set_types(recipe)
        self._set_percentages(recipe)
        self._set_extra_fields(recipe)

    def _set_types(self, recipe):
        self._string_vars['flour_1_type'].set(recipe.flour_type_1)
        self._string_vars['flour_2_type'].set(recipe.flour_type_2)
        self._string_vars['flour_3_type'].set(recipe.flour_type_3)
        self._string_vars['hydration_type_1_type'].set(recipe.hydration_type_1)
        self._string_vars['hydration_type_2_type'].set(recipe.hydration_type_2)
        self._string_vars['fat_type_1_type'].set(recipe.fat_type_1)
        self._string_vars['fat_type_2_type'].set(recipe.fat_type_2)
        self._string_vars['sugar_type'].set(recipe.sugar_type)

    def _set_percentages(self, recipe):
        update_entry(self._entries['flour_1_percentage'], recipe.flour_percentage_1)
        update_entry(self._entries['flour_2_percentage'], recipe.flour_percentage_2)
        update_entry(self._entries['flour_3_percentage'], recipe.flour_percentage_3)
        update_entry(self._entries['hydration_percentage'], recipe.hydration_percentage)
        update_entry(self._entries['hydration_type_1_percentage'], recipe.hydration_type_percentage_1)
        update_entry(self._entries['hydration_type_2_percentage'], recipe.hydration_type_percentage_2)
        update_entry(self._entries['fat_percentage'], recipe.fat_percentage)
        update_entry(self._entries['fat_type_1_percentage'], recipe.fat_type_percentage_1)
        update_entry(self._entries['fat_type_2_percentage'], recipe.fat_type_percentage_2)
        update_entry(self._entries['salt_percentage'], recipe.salt_percentage)
        update_entry(self._entries['sugar_percentage'], recipe.sugar_percentage)

    def _set_extra_fields(self, recipe):
        update_entry(self._entries['leaven_share_percentage'], recipe.leaven_share)
        update_entry(self._entries['leaven_hydration'], recipe.leaven_hydration)
        update_entry(self._entries['poolish_share_percentage'], recipe.poolish_share)
        update_entry(self._entries['poolish_hydration'], recipe.poolish_hydration)
        update_entry(self._entries['tangzhong_share_percentage'], recipe.tangzhong_share)
        update_entry(self._entries['loaf_weight'], recipe.loaf_weight)

    def display_weights(self, weights):
        self._display_flour_weights(weights)
        self._display_liquid_weights(weights)
        self._display_other_weights(weights)

    def _display_flour_weights(self, w):
        update_entry(self._entries['flour_1_weight'], round(w.flour_weight_1))
        update_entry(self._entries['flour_2_weight'], round(w.flour_weight_2))
        update_entry(self._entries['flour_3_weight'], round(w.flour_weight_3))

    def _display_liquid_weights(self, w):
        update_entry(self._entries['hydration_weight'], round(w.hydration_weight))
        update_entry(self._entries['hydration_type_1_weight'], round(w.hydration_type_weight_1))
        update_entry(self._entries['hydration_type_2_weight'], round(w.hydration_type_weight_2))

    def _display_other_weights(self, w):
        update_entry(self._entries['fat_weight'], round(w.fat_weight))
        update_entry(self._entries['fat_type_1_weight'], round(w.fat_type_weight_1))
        update_entry(self._entries['fat_type_2_weight'], round(w.fat_type_weight_2))
        update_entry(self._entries['salt_weight'], round(w.salt_weight))
        update_entry(self._entries['sugar_weight'], round(w.sugar_weight))
        update_entry(self._entries['leaven_share_weight'], round(w.leaven_amount))
        update_entry(self._entries['poolish_share_weight'], round(w.poolish_amount))
        update_entry(self._entries['tangzhong_share_weight'], round(w.tangzhong_amount))
