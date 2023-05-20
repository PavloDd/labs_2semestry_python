from abc import ABC, abstractmethod


class Fridge(ABC):
    """
    First laboratory class in Python programming language
    """
    __instance = None

    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A'):
        self.__brand = brand
        self.__model = model
        self.__capacity_in_liters = capacity_in_liters
        self.__is_defrosing = is_defrosing
        self.__energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosing(self):
        self.__is_defrosing = True

    def turn_off_defrosing(self):
        self.__is_defrosing = False

    def delete_model_info(self):
        self.__model = None

    @property
    def brand(self):
        return self.__brand

    @property
    def energy_efficiency_class(self):
        return self.__energy_efficiency_class

    @abstractmethod
    def get_max_usable_capacity(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Fridge()
        return cls.__instance

    def __str__(self):
        return f"brand={self.__brand}, model={self.__model}, capacity_in_liters={self.__capacity_in_liters}," \
               f" is_defrosing={self.__is_defrosing}, energy_efficiency_class={self.__energy_efficiency_class}"
