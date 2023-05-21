from models.Fridge import Fridge
from typing import List


class FridgeManager:
    """
    Class FridgeManager from second lab
    """
    def __init__(self):
        self.fridges: List[Fridge] = []

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def add_fridges(self, fridges):
        self.fridges.extend(fridges)

    def find_fridges_by_brand(self, brand):
        return [fridge for fridge in self.fridges if fridge.brand == brand]

    def find_fridges_by_energy_efficiency_class(self, energy_efficiency_class):
        return [fridge for fridge in self.fridges
                if fridge.energy_efficiency_class == energy_efficiency_class]
