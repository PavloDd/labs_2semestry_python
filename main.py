class Fridge:
    instance = None

    def __init__(self, brand="Bosch", model="CC11", capacity_in_liters=15, is_defrosing=False,
                 energy_efficiency_class='A'):
        self._brand = brand
        self._model = model
        self._capacity_in_liters = capacity_in_liters
        self._is_defrosing = is_defrosing
        self._energy_efficiency_class = energy_efficiency_class

    def turn_on_defrosing(self):
        self._is_defrosing = True

    def turn_off_defrosing(self):
        self._is_defrosing = False

    def delete_model_info(self):
        del self._model

    @staticmethod
    def get_instance():
        if not Fridge.instance:
            Fridge.instance = Fridge()
        return Fridge.instance

    def __str__(self):
        return f"Fridge(brand={self._brand}, model={self._model}, capacity_in_liters={self._capacity_in_liters}," \
               f" is_defrosing={self._is_defrosing}, energy_efficiency_class={self._energy_efficiency_class})"


fridges = [Fridge("Samsung", "SS13", 15, False, 'A'), Fridge(), Fridge.get_instance(), Fridge.get_instance()]

for fridge in fridges:
    print(fridge)
