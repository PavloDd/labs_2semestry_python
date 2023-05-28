from abc import ABC, abstractmethod


class Fridge(ABC):
    """
    Abstract class Fridge from the second lab
    """
    __instance = None

    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A'):
        """
        Constructor for Fridge objects and objects of its child classes

        Args:
            brand (str): The brand of the fridge.
            model (str): The model of the fridge.
            capacity_in_liters (int): The capacity of the fridge in liters.
            is_defrosing (bool): Indicates whether the fridge has a defrosting feature.
            energy_efficiency_class (str): The energy efficiency class of the fridge.
        """
        self.brand = brand
        self.model = model
        self.capacity_in_liters = capacity_in_liters
        self.is_defrosing = is_defrosing
        self.energy_efficiency_class = energy_efficiency_class
        self.color_available = None

    def get_attribute_by_type(self, attribute_type):
        """
        Returns a dictionary with attributes of a specific data type.

        Args:
            attribute_type (type): The data type of the attributes to be included in the dictionary.

        Returns:
            dict: A dictionary containing attributes of the specified data type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, attribute_type)}

    def __iter__(self):
        """
        Iterates over the available colors of the fridge.

        Returns:
            iter: An iterator over the available colors.
        """
        return iter(self.color_available)

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Abstract method for retrieving the maximum usable capacity of the fridge.

        This method needs to be implemented by the child classes.

        Returns:
            int: The maximum usable capacity of the fridge.
        """
        pass

    @classmethod
    def get_instance(cls):
        """
        Static method that creates an object of any class using the default constructor.

        Returns:
            Fridge: An instance of the class.
        """
        if not cls.__instance:
            cls.__instance = Fridge()
        return cls.__instance

    def __str__(self):
        """
        Returns a string representation of the fridge.

        Returns:
            str: A string representation of the fridge.
        """
        return f"brand={self.brand}, model={self.model}, capacity_in_liters={self.capacity_in_liters}," \
               f" is_defrosing={self.is_defrosing}, energy_efficiency_class={self.energy_efficiency_class}"
