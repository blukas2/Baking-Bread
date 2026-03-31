# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

from config import DEFAULT_VALUES
from recipe import Recipe, RecipeCalculator
from recipe_storage import RecipeStorage
from ui.main_dough_panel import MainDoughPanel
from ui.preferment_panel import PrefermentPanel
from ui.recipe_list_panel import RecipeListPanel
from ui.recipe_card_dialog import RecipeCardDialog
from ui.dialogs import show_info, show_confirmation, show_input_dialog


class BakingBreadApp(tk.Tk):

    def __init__(self, csv_path):
        super().__init__()
        self.title("Baking Bread v0.2 Developer Alpha")
        self._storage = RecipeStorage(csv_path)
        self._calculator = RecipeCalculator()
        self._last_weights = None
        self._build_panels()
        self._load_initial_state()

    def _build_panels(self):
        self._main_panel = MainDoughPanel(
            self, self._on_calculate_all, self._on_calculate_weights, self._on_show_card)
        self._main_panel.grid(row=0, column=0, sticky='n')
        ttk.Separator(self, orient=tk.VERTICAL).grid(row=0, column=1, sticky='ns')
        self._preferment_panel = PrefermentPanel(
            self, self._on_get_amounts, self._on_calculate_preferments, self._on_add_to_dough)
        self._preferment_panel.grid(row=0, column=2, sticky='n')
        ttk.Separator(self, orient=tk.VERTICAL).grid(row=0, column=3, sticky='ns')
        self._recipe_panel = RecipeListPanel(
            self, self._on_recipe_selected, self._on_save, self._on_save_as,
            self._on_delete, self._on_rename, self._on_update_dataset)
        self._recipe_panel.grid(row=0, column=4, sticky='n')

    def _load_initial_state(self):
        default_recipe = Recipe.from_dict(DEFAULT_VALUES)
        self._main_panel.set_recipe(default_recipe)
        self._preferment_panel.set_preferment(default_recipe)
        self._recipe_panel.refresh_list(self._storage.get_recipe_names())

    def _build_current_recipe(self, bread_name=''):
        fields = self._main_panel.get_recipe_fields()
        fields.update(self._preferment_panel.get_preferment_fields())
        fields['bread_name'] = bread_name
        fields['comments'] = self._recipe_panel.get_comments()
        return Recipe.from_dict(fields)

    def _on_calculate_weights(self):
        recipe = self._build_current_recipe()
        self._last_weights = self._calculator.calculate_weights(recipe)
        self._main_panel.display_weights(self._last_weights)

    def _on_calculate_all(self):
        self._on_calculate_weights()
        self._on_get_amounts()
        self._on_calculate_preferments()

    def _on_get_amounts(self):
        if self._last_weights is None:
            return
        self._preferment_panel.set_amounts_from_main(self._last_weights)

    def _on_calculate_preferments(self):
        recipe = self._build_current_recipe()
        if self._last_weights is None:
            self._on_calculate_weights()
        pf_weights = self._calculator.calculate_preferment_weights(recipe, self._last_weights)
        self._preferment_panel.display_weights(pf_weights)

    def _on_add_to_dough(self):
        amounts = self._preferment_panel.get_amounts()
        self._apply_preferment_amounts(amounts)

    def _apply_preferment_amounts(self, amounts):
        from ui.widget_helpers import update_entry
        update_entry(self._main_panel._entries['leaven_share_weight'], round(amounts['leaven_amount']))
        update_entry(self._main_panel._entries['leaven_hydration'], amounts['leaven_hydration'])
        update_entry(self._main_panel._entries['poolish_share_weight'], round(amounts['poolish_amount']))
        update_entry(self._main_panel._entries['poolish_hydration'], amounts['poolish_hydration'])
        update_entry(self._main_panel._entries['tangzhong_share_weight'], round(amounts['tangzhong_amount']))

    def _on_show_card(self):
        self._on_calculate_weights()
        recipe = self._build_current_recipe()
        RecipeCardDialog(self, recipe, self._last_weights)

    def _on_recipe_selected(self, name):
        recipe = self._storage.get_recipe(name)
        if recipe is None:
            return
        self._main_panel.set_recipe(recipe)
        self._preferment_panel.set_preferment(recipe)
        self._recipe_panel.set_comments(recipe.comments)
        self._on_calculate_all()

    def _on_save(self):
        name = self._recipe_panel.get_selected_name()
        if name is None:
            show_info(self, "Save recipe", "No recipe selected, choose one!")
            return
        show_confirmation(self, "Save recipe",
            "WARNING! Are you sure you want to overwrite this recipe?",
            lambda: self._do_save(name))

    def _do_save(self, name):
        recipe = self._build_current_recipe(name)
        self._storage.save_recipe(recipe)
        self._recipe_panel.refresh_list(self._storage.get_recipe_names())

    def _on_save_as(self):
        show_input_dialog(self, "Name your bread!",
            "Enter the name of your new recipe!", self._do_save_as)

    def _do_save_as(self, name):
        if not name or not name.strip():
            show_info(self, "Invalid name!", "The name you entered is invalid. Try another one!")
            return
        recipe = self._build_current_recipe(name)
        self._storage.add_recipe(recipe)
        self._recipe_panel.refresh_list(self._storage.get_recipe_names())

    def _on_delete(self):
        name = self._recipe_panel.get_selected_name()
        if name is None:
            show_info(self, "Delete recipe", "No recipe selected, choose one!")
            return
        show_confirmation(self, "Delete recipe",
            "WARNING! Are you sure you want to delete this recipe?",
            lambda: self._do_delete(name))

    def _do_delete(self, name):
        self._storage.delete_recipe(name)
        self._recipe_panel.refresh_list(self._storage.get_recipe_names())

    def _on_rename(self):
        name = self._recipe_panel.get_selected_name()
        if name is None:
            show_info(self, "Rename recipe", "No recipe selected, choose one!")
            return
        show_input_dialog(self, "Rename your bread!",
            f"You will rename {name} to:", lambda new: self._do_rename(name, new))

    def _do_rename(self, old_name, new_name):
        if not new_name or not new_name.strip():
            show_info(self, "Invalid name!", "The name you entered is invalid. Try another one!")
            return
        if self._storage.name_exists(new_name):
            show_info(self, "Invalid name!", "The name you entered already exists. Try another one!")
            return
        self._storage.rename_recipe(old_name, new_name)
        self._recipe_panel.refresh_list(self._storage.get_recipe_names())

    def _on_update_dataset(self):
        self._storage.write_to_disk()
        show_info(self, "Recipe Book Updated!",
            "Changes successfully updated in the recipe book!")
