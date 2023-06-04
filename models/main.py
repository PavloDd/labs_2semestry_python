"""
Imported classes to make the program work properly
"""
from models.fridge_camera import FridgeCamera
from models.wine_fridge import WineFridge
from manager.fridge_manager import FridgeManager
from manager.set_manager import SetManager
from decorators.decorators import logged


@logged(Exception, "console")
def main():
    """
        Main function that demonstrates the usage of various classes and methods.
    """
    fridges = [FridgeCamera("samsung", "cc112", 23, False, 'B', 1, "mechanic", 3, 100), FridgeCamera(), WineFridge()]
    # fridge_manager = FridgeManager()
    # fridge_manager.add_fridges(fridges)
    #
    # fridge_manager.enumerating()
    # print("\n")
    #
    # print(fridge_manager.zipping())
    # print("\n")
    #
    # bosch_fridges = fridge_manager.find_fridges_by_brand("bosch")
    # for fridge in bosch_fridges:
    #     print(fridge)
    # print("\n")
    #
    # a_class_fridges = fridge_manager.find_fridges_by_energy_efficiency_class('A')
    # for fridge in a_class_fridges:
    #     print(fridge)
    # print("\n")
    #
    # print(fridge_manager.results_of_get_max_usable_capacity())
    # print("\n")
    #
    # print(fridge_manager.check_capacity_of_fridges_all_any(15))
    # print("\n")
    #
    # for i in fridge_manager.fridges:
    #     print(i.get_attribute_by_type(int))
    #
    # set_manager = SetManager(fridge_manager)
    # set_manager.__getitem__(1)
    fridges[0].turn_off_defrosing()


if __name__ == "__main__":
    main()
