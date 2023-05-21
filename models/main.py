from models.FridgeCamera import FridgeCamera
from models.WineFridge import WineFridge
from manager.FridgeManager import FridgeManager


def main():
    fridges = [FridgeCamera("samsung", "cc112", 23, False, 'B', 1, "mechanic", 3, 100), FridgeCamera(), WineFridge()]
    fridge_manager = FridgeManager()
    fridge_manager.add_fridges(fridges)
    bosch_fridges = fridge_manager.find_fridges_by_brand("bosch")
    a_class_fridges = fridge_manager.find_fridges_by_energy_efficiency_class('A')

    for fridge in fridges:
        print(fridge)

    print("\n")

    for fridge in bosch_fridges:
        print(fridge)

    print("\n")

    for fridge in a_class_fridges:
        print(fridge)

    print("\n")

    for fridge in fridges:
        print(fridge.get_max_usable_capacity())


if __name__ == "__main__":
    main()
