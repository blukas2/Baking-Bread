# -*- coding: utf-8 -*-
import tkinter as tk

from config import TITLE_FONT


class RecipeCardDialog(tk.Toplevel):

    def __init__(self, parent, recipe, weights):
        super().__init__(parent)
        self.title('Recipe card')
        self._current_row = 0
        self._add_title(recipe.bread_name)
        self._add_ingredients(recipe, weights)
        self._add_leaven_line(recipe, weights)
        self._add_export_button()

    def _add_title(self, bread_name):
        title = bread_name if bread_name else "Recipe"
        label = tk.Label(self, text=title, font=TITLE_FONT, anchor=tk.CENTER)
        label.grid(row=self._current_row)
        self._current_row += 1

    def _add_ingredients(self, recipe, weights):
        ingredients = self._build_ingredient_list(recipe, weights)
        for amount, name in ingredients:
            if amount != 0:
                self._add_item_line(amount, name)

    def _build_ingredient_list(self, recipe, weights):
        return [
            (weights.flour_weight_1, recipe.flour_type_1),
            (weights.flour_weight_2, recipe.flour_type_2),
            (weights.flour_weight_3, recipe.flour_type_3),
            (weights.hydration_type_weight_1, recipe.hydration_type_1),
            (weights.hydration_type_weight_2, recipe.hydration_type_2),
            (weights.fat_type_weight_1, recipe.fat_type_1),
            (weights.fat_type_weight_2, recipe.fat_type_2),
            (weights.salt_weight, "salt"),
            (weights.sugar_weight, recipe.sugar_type),
        ]

    def _add_item_line(self, amount, name):
        text = f"{round(amount)}g {name}"
        label = tk.Label(self, text=text)
        label.grid(row=self._current_row, sticky='w')
        self._current_row += 1

    def _add_leaven_line(self, recipe, weights):
        if weights.leaven_amount == 0:
            return
        hydration_note = f"({recipe.leaven_hydration}% hydration)"
        text = f"{round(weights.leaven_amount)}g leaven {hydration_note}"
        label = tk.Label(self, text=text)
        label.grid(row=self._current_row, sticky='w')
        self._current_row += 1

    def _add_export_button(self):
        btn = tk.Button(self, text="Export", state=tk.DISABLED)
        btn.grid(row=self._current_row)
