
#A Fishing Game
import random
import time
from fish import fishes
from rod import rods

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
    print("*")
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
    print("*")
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
