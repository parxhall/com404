class Bot:
    def __init__(self, name = "paris", age = 21, energy = 7, shield = 100):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("*" * (len(self.name) + 4))
        print("*", self.name, "*")
        print("*" * (len(self.name) + 4))

    def display_age(self):
        print("""() () ()
|| || ||
********
|      |
| """, self.age,""" |
|______|""")

    def display_energy(self):
        print("❥"*self.energy)

    def display_shield(self):
        print("""|\\______/|
|        |
|   """+ str(self.shield) +"""  |
\\        /
 \\      /
  \\____/""")

    def display_summary(self):
        print("*" * (len(self.name) + 4))
        print("*", self.name, "*")
        print("*" * (len(self.name) + 4))
        print("*" * (len(str(self.age)) + 4))
        print("*", self.age, "*")
        print("*" * (len(str(self.age)) + 4))
        print("*" * (len(str(self.energy)) + 4))
        print("*", self.energy, "*")
        print("*" * (len(str(self.energy)) + 4))
        print("*" * (len(str(self.shield)) + 4))
        print("*", self.shield, "*")
        print("*" * (len(str(self.shield)) + 4))

    def __str__(self):
        print("name = {} \nage = {} \nenergy = {} \nshield = {}".format(self.name,self.age,self.energy,self.shield))

greg = Bot("greg")
greg.display_name()
greg.display_age()
greg.display_energy()
greg.display_shield()
greg.display_summary()
greg.__str__()