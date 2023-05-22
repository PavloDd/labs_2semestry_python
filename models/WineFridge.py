"""
Imported parent class
"""
from .Fridge import Fridge


class WineFridge(Fridge):
    """
    Class WineFridge from second lab
    """
    def __init__(self, brand="bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A', capacity_in_number_of_liters=12,
                 max_volume_of_bottle_in_liters=2):
        """
        Constructor for WineFridge objects, with super().constructor from class Fridge
        """
        super().__init__(brand, model, capacity_in_liters, is_defrosing, energy_efficiency_class)
        self.capacity_in_number_of_liters = capacity_in_number_of_liters
        self.max_volume_of_bottle_in_liters = max_volume_of_bottle_in_liters

    def get_max_usable_capacity(self):
        """
        Override method from abstract class Fridge, which returns max usable capacity of fridge in liters
        """
        return self.capacity_in_number_of_liters * self.max_volume_of_bottle_in_liters

    def __str__(self):
        return f"WineFridge({super().__str__()}, capacity_in_number_of_liters={self.capacity_in_number_of_liters}," \
               f"max_volume_of_bottle_in_liters={self.max_volume_of_bottle_in_liters})"
