

#A Fishing Game


rod_choice = int(print(input("""
Choose your rod, type 1-4:
1 - Cane Pole
2 - Carbon Fiber
3 - Mickey Mouse
4 - Fiber Glass
""")))




class Fish:
    def __init__(self, species, size, hunger, feistiness):
        self.species = species
        self.size = size
        self.hunger = hunger
        self.feistiness = feistiness



class Rod:
    def __init__(self, name, flex, length):
        self.name = name
        self.flex = flex
        self.length = length

    

fish1 = Fish("Minnow", 1, 6, 3)
fish2 = Fish("Perch", 4, 3, 2)
fish3 = Fish("Catfish", 8, 4, 2)
fish4 = Fish("Smallmouth Bass", 6, 5, 5)
fish5 = Fish("Turtle", 4, 2, 1)
fish6 = Fish("Golden Trout", 3, 1, 7)

rod1 = Rod("Cane Pole", 3, 6)
rod2 = Rod("Carbon Fiber", 8, 8)
rod3 = Rod("Mickey Mouse", 2, 1)
rod4 = Rod("Fiber Glass", 5, 5)

