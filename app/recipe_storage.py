# -*- coding: utf-8 -*-
import os
import shutil

import pandas as pd

from config import CSV_COLUMN_MAP
from recipe import Recipe


class RecipeStorage:

    def __init__(self, csv_path):
        self._csv_path = csv_path
        self._backup_dir = os.path.join(os.path.dirname(csv_path), 'dataset_saves')
        self._recipes = {}
        self._load_from_disk()

    def _load_from_disk(self):
        dataframe = pd.read_csv(self._csv_path)
        dataframe = dataframe.rename(columns=CSV_COLUMN_MAP)
        for _, row in dataframe.iterrows():
            recipe = Recipe.from_dict(row.to_dict())
            self._recipes[recipe.bread_name] = recipe

    def get_recipe_names(self):
        return sorted(self._recipes.keys(), reverse=True)

    def get_recipe(self, name):
        return self._recipes.get(name)

    def save_recipe(self, recipe):
        self._recipes[recipe.bread_name] = recipe

    def add_recipe(self, recipe):
        self._recipes[recipe.bread_name] = recipe

    def delete_recipe(self, name):
        self._recipes.pop(name, None)

    def rename_recipe(self, old_name, new_name):
        recipe = self._recipes.pop(old_name, None)
        if recipe is None:
            return False
        recipe.bread_name = new_name
        self._recipes[new_name] = recipe
        return True

    def name_exists(self, name):
        return name in self._recipes

    def write_to_disk(self):
        self._rotate_backups()
        self._save_csv()

    def _rotate_backups(self):
        old2 = os.path.join(self._backup_dir, 'old2_breadDataset.csv')
        old3 = os.path.join(self._backup_dir, 'old3_breadDataset.csv')
        shutil.copy2(old2, old3)
        old1 = os.path.join(self._backup_dir, 'old1_breadDataset.csv')
        shutil.copy2(old1, old2)
        shutil.copy2(self._csv_path, old1)

    def _save_csv(self):
        rows = [r.to_dict() for r in self._recipes.values()]
        dataframe = pd.DataFrame(rows)
        dataframe = dataframe.sort_values('bread_name', ascending=False, ignore_index=True)
        dataframe.to_csv(self._csv_path, index=False)
