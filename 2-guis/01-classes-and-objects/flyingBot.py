from superBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name = "paris", age = 21, energy = 7, shield = 100, power_level = 10, hover = 1):
        super().__init__(name = "paris", age = 21, energy = 7, shield = 100, power_level= 10)
        self.__hover = hover

    def get_hover_distance(self):
        return(self.__hover)

    def set_hover_distance(self):
        self.__hover = input("What is your hover distance?\n")
