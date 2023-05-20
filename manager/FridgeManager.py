from models.Fridge import Fridge
from models.WineFridge import WineFridge
from models.FridgeCamera import FridgeCamera
from typing import List


class FridgeManager:

    def __init__(self):
        self.__fridges: List[Fridge] = []

    def add_fridge(self, fridge):
        self.__fridges.append(fridge)

    def add_fridges(self, fridges):
        self.__fridges.extend(fridges)

    @property
    def fridges(self):
        return self.__fridges

    def find_fridges_by_brand(self, brand):
        return [fridge for fridge in self.__fridges if fridge.brand.__eq__(brand)]

    def find_fridges_by_energy_efficiency_class(self, energy_efficiency_class):
        return [fridge for fridge in self.__fridges
                if fridge.energy_efficiency_class.__eq__(energy_efficiency_class)]
