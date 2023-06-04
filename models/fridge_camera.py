"""
Imported parent class
"""
from .fridge import Fridge


class FridgeCameraException(Exception):
    pass


class FridgeCamera(Fridge):
    """
    Class FridgeCamera from second lab
    """
    __VOLUME_PER_KILOGRAM = 2

    def __init__(self, brand="bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A', number_of_entrances=1, type_of_tape_drive="mechanic",
                 max_tape_speed_in_meters_per_sec=2, max_weight_tape_can_withstand=90):
        """
        Constructor for FridgeCamera objects, with super().constructor from class Fridge
        """
        super().__init__(brand, model, capacity_in_liters, is_defrosing, energy_efficiency_class)
        self.number_of_entrances = number_of_entrances
        self.type_of_tape_drive = type_of_tape_drive
        self.max_tape_speed_in_meters_per_sec = max_tape_speed_in_meters_per_sec
        self.max_weight_tape_can_withstand = max_weight_tape_can_withstand
        self.color_available = {"white", "black", "grey"}

    def get_max_usable_capacity(self):
        """
        Override method from abstract class Fridge, that returns max usable capacity of fridge in liters
        """
        capacity = self.max_weight_tape_can_withstand / self.__VOLUME_PER_KILOGRAM
        if capacity.__eq__(0):
            raise FridgeCameraException("This fridge camera has no useful capacity. Try another one!")
        return capacity

    def __str__(self):
        return f"FridgeCamera({super().__str__()}, number_of_entrances={self.number_of_entrances}," \
                                f" type_of_tape_drive={self.type_of_tape_drive}," \
                                f"max_tape_speed_in_meters_per_sec={self.max_tape_speed_in_meters_per_sec}," \
                                f"__max_weight_tape_can_withstand={self.max_weight_tape_can_withstand})"
