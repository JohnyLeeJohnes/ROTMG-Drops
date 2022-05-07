class Boss:

    # Get drop by name
    def getDrop(self, dropname):
        for drop in self.drops:
            if drop.name == dropname:
                return drop

    # Print boss stats
    def printBoss(self):
        print("Boss: " + self.name + " -  Count: " + str(self.count))
        for drop in self.drops:
            drop.printDrop(self.count)

    # Constructor
    def __init__(self, name):
        self.name = name
        self.count = 1
        self.drops = []
