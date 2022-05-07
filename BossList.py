# Imports
from Boss import Boss
from Drop import Drop


class BossList:

    # Get boss by name
    def getBoss(self, bossname):
        for boss in self.bosses:
            if boss.name == bossname:
                return boss

    # Add uniqe boss to data pool
    def addBoss(self, bossname):
        boss = self.getBoss(bossname)
        if boss:
            boss.count += 1
        else:
            self.bosses.append(Boss(bossname))

    # Add drops to data pool
    def addDrops(self, bossname, bossdrops):
        boss = self.getBoss(bossname)
        for dropname in bossdrops:
            if dropname:
                drop = boss.getDrop(dropname)
                if not drop:
                    boss.drops.append(Drop(dropname))
                else:
                    drop.count += 1

    # Print bosses info
    def printBosses(self):
        for boss in self.bosses:
            boss.printBoss()
            print("----------")

    # Constructor
    def __init__(self):
        self.bosses = []
