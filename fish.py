import random

class Fish:
    def __init__(self, species, size, feistiness,hunger = random.randint(0, 8)):
        self.species = species
        self.size = size
        self.feistiness = feistiness
        self.hunger = hunger
        self.on_rod = None

    def take_bait(self, rod):
        if self.hunger >= 0:    #fish will always not take bait in this setting
            print(f"*** A {self.species.upper()} has taken the bait! ***\n")
            self.on_rod = rod 
            rod.fish = self  #not sure what this is doing
        else:
            print(f"***The {self.species.upper()} got away. ***")
            exit()

    def got_away(self, rod):
        if self.size > self.on_rod.length:
            print(f"The {self.species} got away!")
            self.on_rod = rod 
            rod.fish = self  #not sure what this is doing
            exit()

    def catch_fish(self, rod):
        if self.feistiness < self.on_rod.flex:
            print(f"You caught a very impressive {self.species}!")
            self.on_rod = rod 
            rod.fish = self  #not sure what this is doing
            exit()
        else:
            print(f"Your {self.species} got away. That fish was too feisty!")
            exit()

fish1 = Fish("Minnow", 1, 3)    #species, size, fiestiness, hunger randomized and not shown
fish2 = Fish("Perch", 3, 2)
fish3 = Fish("Catfish", 8, 2)
fish4 = Fish("Smallmouth Bass", 6, 5)
fish5 = Fish("Turtle", 5, 1)
fish6 = Fish("Golden Trout", 4, 7)

fishes = [fish1, fish2, fish3, fish4, fish5, fish6]