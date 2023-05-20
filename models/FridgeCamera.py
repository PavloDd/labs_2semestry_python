from .Fridge import Fridge


class FridgeCamera(Fridge):
    """
    Class FridgeCamera from second lab
    """
    __VOLUME_PER_KILOGRAM = 2

    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A', number_of_entrances=1, type_of_tape_drive="mechanic",
                 max_tape_speed_in_meters_per_sec=2, max_weight_tape_can_withstand=90):
        super().__init__(brand, model, capacity_in_liters, is_defrosing, energy_efficiency_class)
        self.__number_of_entrances = number_of_entrances
        self.__type_of_tape_drive = type_of_tape_drive
        self.__max_tape_speed_in_meters_per_sec = max_tape_speed_in_meters_per_sec
        self.__max_weight_tape_can_withstand = max_weight_tape_can_withstand

    def get_max_usable_capacity(self):
        return self.__max_weight_tape_can_withstand / self.__VOLUME_PER_KILOGRAM

    def __str__(self):
        return f"FridgeCamera({super().__str__()}, number_of_entrances={self.__number_of_entrances}," \
                                f" type_of_tape_drive={self.__type_of_tape_drive}," \
                                f"max_tape_speed_in_meters_per_sec={self.__max_tape_speed_in_meters_per_sec}," \
                                f"__max_weight_tape_can_withstand={self.__max_weight_tape_can_withstand})"

    @property
    def brand(self):
        return self.__brand

    @property
    def energy_efficiency_class(self):
        return self.__energy_efficiency_class

