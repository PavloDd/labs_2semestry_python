from models.Fridge import Fridge


class FridgeManager:
    """
    Class FridgeManager from second lab
    """
    def __init__(self):
        """
        Constructor for FridgeManager objects
        """
        self.fridges: list[Fridge] = []

    def add_fridge(self, fridge):
        """
        Method that adds the object to the list of FridgeManager object
        """
        self.fridges.append(fridge)

    def add_fridges(self, fridges):
        """
        Method that adds the list of objects to the list of FridgeManager object
        """
        self.fridges.extend(fridges)

    def find_fridges_by_brand(self, brand):
        """
        Method that finds the object with the specified parameter
        """
        return [fridge.model for fridge in self.fridges if fridge.brand == brand]

    def find_fridges_by_energy_efficiency_class(self, energy_efficiency_class):
        """
        Method that finds the object with the specified parameter
        """
        return [fridge for fridge in self.fridges
                if fridge.energy_efficiency_class == energy_efficiency_class]


