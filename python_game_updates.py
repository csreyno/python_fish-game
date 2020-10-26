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

while True:
    rods[rod_input].cast_rod()  #choose your own rod
    random_fish = random.randint(0, 5) # chooses a random fish between index 0 -5 from list of fish
    fishes[random_fish].take_bait(rods[rod_input]) #random fish takes bait or doesnt take bait, reel slowly or quickly
    rods[rod_input].reel_rod() #increase or decrease flex based on input
    rods[rod_input].break_rod()                 #rod will break and print if fish size > rod flex
    fishes[random_fish].got_away(rods[rod_input])   #fish will get away if fish size > rod length
    fishes[random_fish].catch_fish(rods[rod_input]) #catch fish if fish fiestiness < rod flex or fish gets away


        # "see if fish takes bite"
            # conditional check for is there a fish on rod
                #stay and reel
                    #until caught or breaks
                # "fish caught or got away"