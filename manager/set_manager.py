from .fridge_manager import FridgeManager
from decorators.decorators import count_args
from decorators.decorators import calls_limit


class SetManager:
    def __init__(self, manager: FridgeManager):
        """
        Constructor for SetManager objects.

        Args:
            manager (FridgeManager): The FridgeManager object to be associated with SetManager.
        """
        self.manager = manager
        self.index = 0

    @calls_limit
    def __len__(self):
        """
        Calculates and returns the total number of color_available across all fridges in the associated FridgeManager.

        Returns:
            int: The total number of color_available.
        """
        length = 0
        for fridge in self.manager:
            length += len(fridge.color_available)
        return length

    @calls_limit
    def __iter__(self):
        """
        Iterates over the color_available across all fridges in the associated FridgeManager.

        Yields:
            Any: The next available color.
        """
        for fridge in self.manager:
            for color_available in fridge.color_available:
                yield color_available

    @calls_limit
    def __next__(self):
        """
        Retrieves the next color_available in the associated FridgeManager.

        Returns:
            Any: The next available color.

        Raises:
            StopIteration: If there are no more colors available.
        """
        if self.index >= len(self.manager):
            raise StopIteration
        self.index += 1
        return self.manager[self.index].color_available

    def unic_items(self):
        unic_items_set = set()
        for fridge in self.manager:
            for color_available in fridge.color_available:
                unic_items_set.add(fridge)


    @count_args
    def __getitem__(self, index):
        """
        Retrieves the color_available at the specified index in the associated FridgeManager.

        Args:
            index (int): The index of the color_available to retrieve.

        Returns:
            Any: The color_available at the specified index.
        """
        return self.manager[index].color_available
