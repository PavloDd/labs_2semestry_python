from Fridge import Fridge


def main():
    fridges = [Fridge("Samsung", "SS13", 15, False, 'A'), Fridge(), Fridge.get_instance(), Fridge.get_instance()]
    for fridge in fridges:
        print(fridge)


if __name__ == "__main__":
    main()
