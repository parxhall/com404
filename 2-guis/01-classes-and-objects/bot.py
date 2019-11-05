# i am creating the class bot which will use all of the following classes and methods
class Bot:
    # here im creating all of the existing attribute
    def __init__(self, name = "paris", age = 21, energy = 7, shield = 100):
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.__shield = shield

    # this section is methods asking for input
    def get_age(self):
        return(self.__age)

    def get_energy(self):
        return(self.__energy)

    def get_name(self):
        return(self.__name)

    def get_shield(self):
        return(self.__shield)

    # the following methods use the attributes define and listed above to display
    def decrement_energy(self):
        de = input(int("how much?\n"))
        self.__energy -= de

    def decrement_shield(self):
        ds = input(int("how much?\n"))
        self.__shield -= ds

    def display_name(self):
        print("*" * (len(self.__name) + 4))
        print("*", self.__name, "*")
        print("*" * (len(self.__name) + 4))

    def display_age(self):
        print("""() () ()
|| || ||
********
|      |
| """, self.__age,""" |
|______|""")

    def display_energy(self):
        print("❥"*self.__energy)

    def display_shield(self):
        print("""|\\______/|
|        |
|   """+ str(self.__shield) +"""  |
\\        /
 \\      /
  \\____/""")

    def display_summary(self):
        print("*" * (len(self.__name) + 4))
        print("*", self.__name, "*")
        print("*" * (len(self.__name) + 4))
        print("*" * (len(str(self.__age)) + 4))
        print("*", self.__age, "*")
        print("*" * (len(str(self.__age)) + 4))
        print("*" * (len(str(self.__energy)) + 4))
        print("*", self.__energy, "*")
        print("*" * (len(str(self.__energy)) + 4))
        print("*" * (len(str(self.__shield)) + 4))
        print("*", self.__shield, "*")
        print("*" * (len(str(self.__shield)) + 4))

    def __str__(self):
        return("name = {} \nage = {} \nenergy = {} \nshield = {}".format(self.__name,self.__age,self.__energy,self.__shield))

    def increment_age(self):
        ia = input(int("by how many birthdays?\n"))
        self.__age += ia

    def increment_energy(self):
        ie = input(int("by how much?\n"))
        self.__energy +=ie

    def increment_shield(self):
        inc_s = input(int("by how much?\n"))
        self.__shield += inc_s

    def set_name(self):
        self.__name = input("What is your name?\n")

