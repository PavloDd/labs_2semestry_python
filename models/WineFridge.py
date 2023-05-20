from .Fridge import Fridge


class WineFridge(Fridge):
    """
    Class WineFridge from second lab
    """
    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A', capacity_in_number_of_liters=12,
                 max_volume_of_bottle_in_liters=2):
        super().__init__(brand, model, capacity_in_liters, is_defrosing, energy_efficiency_class)
        self.__capacity_in_number_of_liters = capacity_in_number_of_liters
        self.__max_volume_of_bottle_in_liters = max_volume_of_bottle_in_liters

    def get_max_usable_capacity(self):
        return self.__capacity_in_number_of_liters * self.__max_volume_of_bottle_in_liters

    def __str__(self):
        return f"WineFridge({super().__str__()}, capacity_in_number_of_liters={self.__capacity_in_number_of_liters}," \
               f"max_volume_of_bottle_in_liters={self.__max_volume_of_bottle_in_liters})"

    @property
    def brand(self):
        return self.__brand

    @property
    def energy_efficiency_class(self):
        return self.__energy_efficiency_class

