
#A Fishing Game
import random
import time



class Fish:
    def __init__(self, species, size, feistiness,hunger = random.randint(0, 8)):
        self.species = species
        self.size = size
        self.feistiness = feistiness
        self.hunger = hunger
        self.on_rod = None

    def take_bait(self, rod):
        if self.hunger >= 9:    #fish will always not take bait in this setting
            print(f"*** A {self.species.upper()} has taken the bait! ***\n")
            self.on_rod = rod 
            rod.fish = self  #not sure what this is doing
        else:
            Rod.cast_again()      #how to run conditional "cast_again" method here
            self.on_rod = rod
            rod.fish = self

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

class Rod:
    def __init__(self, name, flex, length):
        self.name = name
        self.flex = flex
        self.length = length
        self.fish = None

    def cast_rod(self):
        print(f"You cast your {self.name} rod.")
    
    def cast_again(self):
        recast = int(input(f"A {self.fish.species} looked at your bait but swam away.\n\nCast again?\n1 - Yes\n2 - No\n"))
        if recast == 1:
            exit()          #how to loop back to cast_rod
        elif recast == 2:
            print("Ok bye!")
            exit()

    def break_rod(self):
        if self.fish.size > self.flex:
            print(f"The {self.fish.species} broke your {self.name} rod!")
            exit()

    def reel_rod(self):
        choice = int(input("How would you like to reel your rod?\n1 - In a stately manner\n2 - Furiously!!\n"))
        if choice == 1:
            self.flex += 2
        elif choice == 2:
            self.flex -= 2
            

fish1 = Fish("Minnow", 1, 3)    #species, size, fiestiness, hunger randomized and not shown
fish2 = Fish("Perch", 3, 2)
fish3 = Fish("Catfish", 8, 2)
fish4 = Fish("Smallmouth Bass", 6, 5)
fish5 = Fish("Turtle", 5, 1)
fish6 = Fish("Golden Trout", 4, 7)

fishes = [fish1, fish2, fish3, fish4, fish5, fish6]

rod1 = Rod("Cane Pole", 4, 6)       #type, flex, length
rod2 = Rod("Carbon Fiber", 9, 8)
rod3 = Rod("Mickey Mouse", 2, 1)  #flex is 2
rod4 = Rod("Fiberglass", 6, 5)

rods = [rod1, rod2, rod3, rod4]

rod_input = int(input("""
Choose your rod, type 1-4:
1 - Cane Pole
2 - Carbon Fiber
3 - Mickey Mouse
4 - Fiber Glass
""")) - 1


#============================================

rods[rod_input].cast_rod()          #choose your own rod

starttime = time.time()
i = 0       #random seconds count bewtween 0-3 for impression of waiting for a fish to take bait
while i <= random.randint(0, 1):
    print(".")
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    i += 1

random_fish = random.randint(0, 5)   # chooses a random fish between index 0 -5 from the above list of fish

fishes[random_fish].take_bait(rods[rod_input])     #random fish takes bait or doesnt take bait, reel slowly or quickly

# rods[rod_input].cast_again()                #cast again branch

rods[rod_input].reel_rod()                         #increase or decrease flex based on input

# print(rods[rod_input].flex)       #flex increasing or decreasing properly

starttime = time.time()
i = 0       #random seconds count bewtween 0-2 for impression of reeling the fish in
while i <= random.randint(1, 1):
    print(".")
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    i += 1

rods[rod_input].break_rod()                 #rod will break and print if fish size > rod flex
fishes[random_fish].got_away(rods[rod_input])   #fish will get away if fish size > rod length
fishes[random_fish].catch_fish(rods[rod_input])   #catch fish if fish fiestiness < rod flex or fish gets away



#need to integrate fiestiness attribute
#add what to do if fish doesnt take bait path
#adjust adjust values as needed for rod and fish to get believable outcomes


# rod4.cast_rod()
# fish3.take_bait(rod4)
# fish3.catch_fish()
