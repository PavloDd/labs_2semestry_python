from models.fridge import Fridge
from decorators.decorators import count_args
from decorators.decorators import calls_limit


class FridgeManager:
    """
    Class FridgeManager from the second lab
    """
    def __init__(self):
        """
        Constructor for FridgeManager objects
        """
        self.fridges: list[Fridge] = []

    def __getitem__(self, index):
        """
        Retrieves the fridge at the specified index.

        Args:
            index (int): The index of the fridge to retrieve.

        Returns:
            Fridge: The fridge object at the specified index.
        """
        return self.fridges[index]

    @calls_limit
    def __len__(self):
        """
        Returns the number of fridges in the FridgeManager.

        Returns:
            int: The number of fridges in the FridgeManager.
        """
        return len(self.fridges)

    @calls_limit
    def __iter__(self):
        """
        Returns an iterator over the fridges in the FridgeManager.

        Returns:
            iter: An iterator over the fridges.
        """
        return iter(self.fridges)

    @count_args
    def fridges_to_string(self):
        """
        Transforms a list of Fridge objects into a list of strings.

        Returns:
            list: A list of string representations of the fridges.
        """
        fridges_to_string = []
        for fridge in self.fridges:
            fridges_to_string.append(fridge.__str__())
        return fridges_to_string

    @count_args
    def results_of_get_max_usable_capacity(self):
        """
        Applies the get_max_usable_capacity method to every element in the list and returns a list of results.

        Returns:
            list: A list of results from the get_max_usable_capacity method.
        """
        result = []
        for fridge in self.fridges:
            result.append(fridge.get_max_usable_capacity())
        return result

    @calls_limit
    def enumerating(self):
        """
        Enumerates every Fridge object in the FridgeManager list fridges.
        """
        for i, fridge_str in enumerate(self.fridges_to_string()):
            print(i, fridge_str)

    @count_args
    def zipping(self):
        """
        Zips two lists (list of Fridge objects and list from results_of_get_max_usable_capacity) into one.
        """
        _zipped_list = zip(self.fridges_to_string(), self.results_of_get_max_usable_capacity())
        for item in _zipped_list:
            print(item)

    @count_args
    def check_capacity_of_fridges_all_any(self, needed_capacity):
        """
        Checks if all or any fridges have a capacity greater than the specified value.

        Args:
            needed_capacity (int): The capacity threshold.

        Returns:
            dict: A dictionary indicating whether all or any fridges satisfy the condition.
        """
        all_satisfy = all(fridge.capacity_in_liters > needed_capacity for fridge in self.fridges)
        any_satisfy = any(fridge.capacity_in_liters > needed_capacity for fridge in self.fridges)
        return {"All": all_satisfy, "Any": any_satisfy}

    def add_fridge(self, fridge):
        """
        Adds a fridge object to the list of FridgeManager objects.

        Args:
            fridge (Fridge): The fridge object to be added.
        """
        self.fridges.append(fridge)

    def add_fridges(self, fridges):
        """
        Adds a list of fridge objects to the list of FridgeManager objects.

        Args:
            fridges (list): The list of fridge objects to be added.
        """
        self.fridges.extend(fridges)

    def find_fridges_by_brand(self, brand):
        """
        Finds fridge objects with the specified brand.

        Args:
            brand (str): The brand to search for.

        Returns:
            list: A list of fridge objects with the specified brand.
        """
        return [fridge for fridge in self.fridges if fridge.brand == brand]

    def find_fridges_by_energy_efficiency_class(self, energy_efficiency_class):
        """
        Finds fridge objects with the specified energy efficiency class.

        Args:
            energy_efficiency_class (str): The energy efficiency class to search for.

        Returns:
            list: A list of fridge objects with the specified energy efficiency class.
        """
        return [fridge for fridge in self.fridges if fridge.energy_efficiency_class == energy_efficiency_class]
