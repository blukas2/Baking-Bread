# -*- coding: utf-8 -*-
import tkinter as tk

from config import FLOUR_TYPES, TITLE_FONT
from ui.widget_helpers import (
    create_ingredient_row, create_entry, create_labeled_row,
    add_separator, update_entry
)


class PrefermentPanel(tk.Frame):

    def __init__(self, parent, on_get_amounts, on_calculate, on_add_to_dough):
        super().__init__(parent)
        self._string_vars = {}
        self._entries = {}
        self._current_row = 0
        self._build_header()
        self._build_leaven_section()
        self._build_poolish_section()
        self._build_tangzhong_section()
        self._build_buttons(on_get_amounts, on_calculate, on_add_to_dough)

    def _build_header(self):
        tk.Label(self, text="Pre-ferments", font=TITLE_FONT, anchor=tk.CENTER).grid(
            row=0, column=0)
        tk.Label(self, text="Baker's %", font=TITLE_FONT, anchor=tk.CENTER).grid(
            row=0, column=1)
        tk.Label(self, text="Weight (g)", font=TITLE_FONT, anchor=tk.CENTER).grid(
            row=0, column=2)
        self._current_row = 1
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _add_amount_row(self, label_text, key):
        tk.Label(self, text=label_text).grid(
            row=self._current_row, column=0, columnspan=2)
        entry = create_entry(self)
        entry.grid(row=self._current_row, column=2)
        self._entries[key + '_amount'] = entry
        self._current_row += 1

    def _add_flour_row(self, key_prefix):
        var = tk.StringVar()
        self._string_vars[key_prefix + '_type'] = var
        _, perc, weight = create_ingredient_row(self, var, FLOUR_TYPES, self._current_row, 0)
        self._entries[key_prefix + '_percentage'] = perc
        self._entries[key_prefix + '_weight'] = weight
        self._current_row += 1

    def _add_hydration_row(self, key):
        _, perc, weight = create_labeled_row(self, "Hydration", self._current_row, 0)
        self._entries[key + '_hydration_percentage'] = perc
        self._entries[key + '_hydration_weight'] = weight
        self._current_row += 1

    def _build_leaven_section(self):
        self._add_amount_row("Leaven", 'leaven')
        self._add_flour_row('leaven_flour_1')
        self._add_flour_row('leaven_flour_2')
        self._add_hydration_row('leaven')
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_poolish_section(self):
        self._add_amount_row("Poolish", 'poolish')
        self._add_flour_row('poolish_flour_1')
        self._add_flour_row('poolish_flour_2')
        self._add_hydration_row('poolish')
        self._build_poolish_leaven_rows()
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_poolish_leaven_rows(self):
        _, perc, amount = create_labeled_row(self, "Leaven", self._current_row, 0)
        self._entries['poolish_leaven_share'] = perc
        self._entries['poolish_leaven_amount'] = amount
        self._current_row += 1
        tk.Label(self, text="Leaven hydration").grid(row=self._current_row, column=0)
        entry = create_entry(self)
        entry.grid(row=self._current_row, column=1)
        self._entries['poolish_leaven_hydration'] = entry
        self._current_row += 1

    def _build_tangzhong_section(self):
        self._add_amount_row("Tangzhong", 'tangzhong')
        var = tk.StringVar()
        self._string_vars['tangzhong_flour_type'] = var
        _, _, weight = create_ingredient_row(self, var, FLOUR_TYPES, self._current_row, 0)
        self._entries['tangzhong_flour_weight'] = weight
        self._current_row += 1
        tk.Label(self, text="Hydration").grid(row=self._current_row, column=0)
        entry = create_entry(self)
        entry.grid(row=self._current_row, column=2)
        self._entries['tangzhong_hydration_weight'] = entry
        self._current_row += 1
        add_separator(self, self._current_row, 0)
        self._current_row += 1

    def _build_buttons(self, on_get, on_calculate, on_add):
        tk.Button(self, text="Get amounts", command=on_get, width=16).grid(
            row=self._current_row, column=0)
        tk.Button(self, text="Calculate weight", command=on_calculate).grid(
            row=self._current_row, column=1)
        btn_perc = tk.Button(self, text="Calculate %s", state=tk.DISABLED)
        btn_perc.grid(row=self._current_row, column=2)
        self._current_row += 1
        tk.Button(self, text="Add to the dough", command=on_add, width=16).grid(
            row=self._current_row, column=0)

    def get_preferment_fields(self):
        return {
            'leaven_flour_type_1': self._string_vars['leaven_flour_1_type'].get(),
            'leaven_flour_type_2': self._string_vars['leaven_flour_2_type'].get(),
            'leaven_flour_percentage_1': self._get_float('leaven_flour_1_percentage'),
            'leaven_flour_percentage_2': self._get_float('leaven_flour_2_percentage'),
            'poolish_flour_type_1': self._string_vars['poolish_flour_1_type'].get(),
            'poolish_flour_type_2': self._string_vars['poolish_flour_2_type'].get(),
            'poolish_flour_percentage_1': self._get_float('poolish_flour_1_percentage'),
            'poolish_flour_percentage_2': self._get_float('poolish_flour_2_percentage'),
            'poolish_leaven_share': self._get_float('poolish_leaven_share'),
            'poolish_leaven_hydration': self._get_float('poolish_leaven_hydration'),
            'tangzhong_flour_type': self._string_vars['tangzhong_flour_type'].get(),
        }

    def _get_float(self, key):
        value = self._entries[key].get()
        if not value or value.strip() == '':
            return 0.0
        return float(value)

    def set_preferment(self, recipe):
        self._set_types(recipe)
        self._set_percentages(recipe)

    def _set_types(self, recipe):
        self._string_vars['leaven_flour_1_type'].set(recipe.leaven_flour_type_1)
        self._string_vars['leaven_flour_2_type'].set(recipe.leaven_flour_type_2)
        self._string_vars['poolish_flour_1_type'].set(recipe.poolish_flour_type_1)
        self._string_vars['poolish_flour_2_type'].set(recipe.poolish_flour_type_2)
        self._string_vars['tangzhong_flour_type'].set(recipe.tangzhong_flour_type)

    def _set_percentages(self, recipe):
        update_entry(self._entries['leaven_flour_1_percentage'], recipe.leaven_flour_percentage_1)
        update_entry(self._entries['leaven_flour_2_percentage'], recipe.leaven_flour_percentage_2)
        update_entry(self._entries['poolish_flour_1_percentage'], recipe.poolish_flour_percentage_1)
        update_entry(self._entries['poolish_flour_2_percentage'], recipe.poolish_flour_percentage_2)
        update_entry(self._entries['poolish_leaven_share'], recipe.poolish_leaven_share)
        update_entry(self._entries['poolish_leaven_hydration'], recipe.poolish_leaven_hydration)

    def set_amounts_from_main(self, weights):
        update_entry(self._entries['leaven_amount'], round(weights.leaven_amount))
        update_entry(self._entries['leaven_hydration_percentage'], weights.leaven_amount and weights.leaven_amount)
        update_entry(self._entries['poolish_amount'], round(weights.poolish_amount))
        update_entry(self._entries['tangzhong_amount'], round(weights.tangzhong_amount))

    def get_amounts(self):
        return {
            'leaven_amount': self._get_float('leaven_amount'),
            'leaven_hydration': self._get_float('leaven_hydration_percentage'),
            'poolish_amount': self._get_float('poolish_amount'),
            'poolish_hydration': self._get_float('poolish_hydration_percentage'),
            'tangzhong_amount': self._get_float('tangzhong_amount'),
        }

    def display_weights(self, pf_weights):
        self._display_leaven_weights(pf_weights)
        self._display_poolish_weights(pf_weights)
        self._display_tangzhong_weights(pf_weights)

    def _display_leaven_weights(self, w):
        update_entry(self._entries['leaven_flour_1_weight'], round(w.leaven_flour_weight_1))
        update_entry(self._entries['leaven_flour_2_weight'], round(w.leaven_flour_weight_2))
        update_entry(self._entries['leaven_hydration_weight'], round(w.leaven_hydration_weight))

    def _display_poolish_weights(self, w):
        update_entry(self._entries['poolish_flour_1_weight'], round(w.poolish_flour_weight_1))
        update_entry(self._entries['poolish_flour_2_weight'], round(w.poolish_flour_weight_2))
        update_entry(self._entries['poolish_hydration_weight'], round(w.poolish_hydration_weight))
        update_entry(self._entries['poolish_leaven_amount'], round(w.poolish_leaven_amount))

    def _display_tangzhong_weights(self, w):
        update_entry(self._entries['tangzhong_flour_weight'], round(w.tangzhong_flour_weight))
        update_entry(self._entries['tangzhong_hydration_weight'], round(w.tangzhong_hydration_weight))
