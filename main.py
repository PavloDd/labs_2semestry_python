class Fridge:
    instance = None

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
        del self.__model

    @staticmethod
    def get_instance():
        if not Fridge.instance:
            Fridge.instance = Fridge()
        return Fridge.instance

    def __str__(self):
        return f"Fridge(brand={self.__brand}, model={self.__model}, capacity_in_liters={self.__capacity_in_liters}," \
               f" is_defrosing={self.__is_defrosing}, energy_efficiency_class={self.__energy_efficiency_class})"


fridges = [Fridge("Samsung", "SS13", 15, False, 'A'), Fridge(), Fridge.get_instance(), Fridge.get_instance()]

for fridge in fridges:
    print(fridge)
