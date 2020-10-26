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

rod1 = Rod("Cane Pole", 4, 6)       #type, flex, length
rod2 = Rod("Carbon Fiber", 9, 8)
rod3 = Rod("Mickey Mouse", 2, 1)  #flex is 2
rod4 = Rod("Fiberglass", 5, 6)

rods = [rod1, rod2, rod3, rod4]