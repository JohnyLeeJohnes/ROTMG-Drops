# Imports
from BossList import BossList

# Variables
FILE_PATH = 'drops.txt'
BossList = BossList()


def main():
    # Init bosses from file
    file = open(FILE_PATH, "r")

    if file:
        for line in file:
            items = line.strip("\n").split(";")
            bossname = items.pop(0).upper()
            items = [x.lower() for x in items]
            BossList.addBoss(bossname)
            BossList.addDrops(bossname, items)
        BossList.printBosses()


if __name__ == "__main__":
    main()
