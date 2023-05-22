from abc import ABC, abstractmethod


class Fridge(ABC):
    """
    Abstract class Fridge from second lab
    """
    __instance = None

    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A'):
        """
        Constructor for Fridge objects and objects of its child classes
        """
        self.brand = brand
        self.model = model
        self.capacity_in_liters = capacity_in_liters
        self.is_defrosing = is_defrosing
        self.energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosing(self):
        """
        Method that turns on defrosing of the fridge
        """
        self.is_defrosing = True

    def turn_off_defrosing(self):
        """
        Method that turns off defrosing of the fridge
        """
        self.is_defrosing = False

    def delete_model_info(self):
        """
        Method that deletes information about fridge model
        """
        self.model = None

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Empty method for overriding
        """
        pass

    @classmethod
    def get_instance(cls):
        """
        Static method that creates object of any class by default constructor
        """
        if not cls.__instance:
            cls.__instance = Fridge()
        return cls.__instance

    def __str__(self):
        return f"brand={self.brand}, model={self.model}, capacity_in_liters={self.capacity_in_liters}," \
               f" is_defrosing={self.is_defrosing}, energy_efficiency_class={self.energy_efficiency_class}"
