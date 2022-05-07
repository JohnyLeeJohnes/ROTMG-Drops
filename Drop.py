class Drop:

    # Constructor
    def __init__(self, name):
        self.name = name
        self.count = 1

    # Print drop info
    def printDrop(self, bosscount):
        percentage = (self.count / bosscount) * 100
        if percentage > 100:
            percentage = 100
        print("Item: " + self.name + " - Chance: " + str(round(percentage, 2)) + "%")
