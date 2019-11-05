from bot import Bot

class SuperBot(Bot):
    def __init__(self, name = "paris", age = 21, energy = 7, shield = 100, power_level = 10):
        super().__init__(name, age, energy, shield)
        self.__power_level = power_level

    def get_power_level(self):
        return(self.__power_level)

    def set_power_level(self):
        self.__power_level = input("What is your power level?\n")

