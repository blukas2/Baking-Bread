# -*- coding: utf-8 -*-
from dataclasses import dataclass, field, fields, asdict


@dataclass
class Recipe:
    bread_name: str = ''
    flour_type_1: str = 'none'
    flour_type_2: str = 'none'
    flour_type_3: str = 'none'
    flour_percentage_1: float = 0.0
    flour_percentage_2: float = 0.0
    flour_percentage_3: float = 0.0
    hydration_percentage: float = 0.0
    hydration_type_1: str = 'none'
    hydration_type_2: str = 'none'
    hydration_type_percentage_1: float = 0.0
    hydration_type_percentage_2: float = 0.0
    fat_percentage: float = 0.0
    fat_type_1: str = 'none'
    fat_type_2: str = 'none'
    fat_type_percentage_1: float = 0.0
    fat_type_percentage_2: float = 0.0
    salt_percentage: float = 0.0
    sugar_type: str = 'none'
    sugar_percentage: float = 0.0
    leaven_share: float = 0.0
    leaven_hydration: float = 0.0
    poolish_share: float = 0.0
    poolish_hydration: float = 0.0
    tangzhong_share: float = 0.0
    loaf_weight: float = 500.0
    leaven_flour_type_1: str = 'none'
    leaven_flour_type_2: str = 'none'
    leaven_flour_percentage_1: float = 0.0
    leaven_flour_percentage_2: float = 0.0
    poolish_flour_type_1: str = 'none'
    poolish_flour_type_2: str = 'none'
    poolish_flour_percentage_1: float = 0.0
    poolish_flour_percentage_2: float = 0.0
    poolish_leaven_share: float = 0.0
    poolish_leaven_hydration: float = 0.0
    tangzhong_flour_type: str = 'none'
    comments: str = ''

    @classmethod
    def from_dict(cls, data):
        valid_keys = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)

    def to_dict(self):
        return asdict(self)


@dataclass
class CalculatedWeights:
    flour_weight_1: float = 0.0
    flour_weight_2: float = 0.0
    flour_weight_3: float = 0.0
    hydration_weight: float = 0.0
    hydration_type_weight_1: float = 0.0
    hydration_type_weight_2: float = 0.0
    fat_weight: float = 0.0
    fat_type_weight_1: float = 0.0
    fat_type_weight_2: float = 0.0
    salt_weight: float = 0.0
    sugar_weight: float = 0.0
    leaven_amount: float = 0.0
    poolish_amount: float = 0.0
    tangzhong_amount: float = 0.0


@dataclass
class PrefermentWeights:
    leaven_flour_weight_1: float = 0.0
    leaven_flour_weight_2: float = 0.0
    leaven_hydration_weight: float = 0.0
    poolish_flour_weight_1: float = 0.0
    poolish_flour_weight_2: float = 0.0
    poolish_hydration_weight: float = 0.0
    poolish_leaven_amount: float = 0.0
    tangzhong_flour_weight: float = 0.0
    tangzhong_hydration_weight: float = 0.0


class RecipeCalculator:

    def calculate_weights(self, recipe):
        flour_base = self._flour_base_weight(recipe)
        leaven = flour_base * recipe.leaven_share / 100
        poolish = flour_base * recipe.poolish_share / 100
        tangzhong = flour_base * recipe.tangzhong_share / 100
        hydration = self._hydration_weight(recipe, leaven, poolish, tangzhong)
        fat = self._fat_weight(recipe, flour_base, leaven)
        salt = recipe.loaf_weight * recipe.salt_percentage / 100
        sugar = recipe.loaf_weight * recipe.sugar_percentage / 100
        flour_weights = self._flour_type_weights(recipe, flour_base, tangzhong)
        hydration_weights = self._hydration_type_weights(recipe, hydration)
        fat_weights = self._fat_type_weights(recipe, fat)
        return CalculatedWeights(
            flour_weight_1=flour_weights[0],
            flour_weight_2=flour_weights[1],
            flour_weight_3=flour_weights[2],
            hydration_weight=hydration,
            hydration_type_weight_1=hydration_weights[0],
            hydration_type_weight_2=hydration_weights[1],
            fat_weight=fat,
            fat_type_weight_1=fat_weights[0],
            fat_type_weight_2=fat_weights[1],
            salt_weight=salt,
            sugar_weight=sugar,
            leaven_amount=leaven,
            poolish_amount=poolish,
            tangzhong_amount=tangzhong,
        )

    def calculate_preferment_weights(self, recipe, weights):
        leaven = self._leaven_weights(recipe, weights.leaven_amount)
        poolish = self._poolish_weights(recipe, weights.poolish_amount)
        tangzhong = self._tangzhong_weights(weights.tangzhong_amount)
        return PrefermentWeights(
            leaven_flour_weight_1=leaven[0],
            leaven_flour_weight_2=leaven[1],
            leaven_hydration_weight=leaven[2],
            poolish_flour_weight_1=poolish[0],
            poolish_flour_weight_2=poolish[1],
            poolish_hydration_weight=poolish[2],
            poolish_leaven_amount=poolish[3],
            tangzhong_flour_weight=tangzhong[0],
            tangzhong_hydration_weight=tangzhong[1],
        )

    def _flour_base_weight(self, recipe):
        leaven_factor = recipe.leaven_share / 100 / (1 + recipe.leaven_hydration / 100)
        poolish_factor = recipe.poolish_share / 100 / (1 + recipe.poolish_hydration / 100)
        tangzhong_factor = recipe.tangzhong_share / 100 / 6
        return recipe.loaf_weight / (1 + leaven_factor + poolish_factor + tangzhong_factor)

    def _hydration_weight(self, recipe, leaven, poolish, tangzhong):
        total_hydration = recipe.loaf_weight * recipe.hydration_percentage / 100
        leaven_water = leaven * recipe.leaven_hydration / (100 + recipe.leaven_hydration)
        poolish_water = poolish * recipe.poolish_hydration / (100 + recipe.poolish_hydration)
        tangzhong_water = tangzhong * 5 / 6
        return total_hydration - (leaven_water + poolish_water + tangzhong_water)

    def _fat_weight(self, recipe, flour_base, leaven):
        leaven_flour_contribution = leaven * (recipe.leaven_hydration / 100 / 2)
        return (flour_base + leaven_flour_contribution) * recipe.fat_percentage / 100

    def _flour_type_weights(self, recipe, flour_base, tangzhong):
        adjusted_flour = flour_base + tangzhong / 6
        weight_1 = adjusted_flour * recipe.flour_percentage_1 / 100 - tangzhong / 6
        weight_2 = adjusted_flour * recipe.flour_percentage_2 / 100
        weight_3 = adjusted_flour * recipe.flour_percentage_3 / 100
        return (weight_1, weight_2, weight_3)

    def _hydration_type_weights(self, recipe, total_hydration):
        if recipe.hydration_percentage == 0:
            return (0.0, 0.0)
        ratio = 1 / recipe.hydration_percentage
        weight_1 = total_hydration * recipe.hydration_type_percentage_1 * ratio
        weight_2 = total_hydration * recipe.hydration_type_percentage_2 * ratio
        return (weight_1, weight_2)

    def _fat_type_weights(self, recipe, total_fat):
        if total_fat == 0 or recipe.fat_percentage == 0:
            return (0.0, 0.0)
        ratio = 1 / recipe.fat_percentage
        weight_1 = total_fat * recipe.fat_type_percentage_1 * ratio
        weight_2 = total_fat * recipe.fat_type_percentage_2 * ratio
        return (weight_1, weight_2)

    def _leaven_weights(self, recipe, leaven_amount):
        if leaven_amount == 0:
            return (0.0, 0.0, 0.0)
        total_perc = (recipe.leaven_flour_percentage_1
                      + recipe.leaven_flour_percentage_2
                      + recipe.leaven_hydration)
        unit = leaven_amount / total_perc
        flour_1 = unit * recipe.leaven_flour_percentage_1
        flour_2 = unit * recipe.leaven_flour_percentage_2
        hydration = unit * recipe.leaven_hydration
        return (flour_1, flour_2, hydration)

    def _poolish_weights(self, recipe, poolish_amount):
        if poolish_amount == 0:
            return (0.0, 0.0, 0.0, 0.0)
        dry = poolish_amount / (100 + recipe.poolish_hydration) * 100
        wet = poolish_amount / (100 + recipe.poolish_hydration) * recipe.poolish_hydration
        leaven_dry = (recipe.poolish_leaven_share
                      / (100 + recipe.poolish_leaven_hydration) * 100)
        dry_total = (recipe.poolish_flour_percentage_1
                     + recipe.poolish_flour_percentage_2 + leaven_dry)
        if dry_total == 0:
            return (0.0, 0.0, 0.0, 0.0)
        flour_1 = dry / dry_total * recipe.poolish_flour_percentage_1
        flour_2 = dry / dry_total * recipe.poolish_flour_percentage_2
        leaven_wet = (recipe.poolish_leaven_share
                      / (100 + recipe.poolish_leaven_hydration)
                      * recipe.poolish_leaven_hydration)
        wet_total = recipe.poolish_hydration + leaven_wet
        hydration = wet / wet_total * recipe.poolish_hydration if wet_total else 0.0
        leaven_amount = (flour_1 + flour_2) * recipe.poolish_leaven_share / 100
        return (flour_1, flour_2, hydration, leaven_amount)

    def _tangzhong_weights(self, tangzhong_amount):
        if tangzhong_amount == 0:
            return (0.0, 0.0)
        flour = tangzhong_amount / 6
        hydration = tangzhong_amount / 6 * 5
        return (flour, hydration)
