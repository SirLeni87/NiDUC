from src.Pig import Pig
from src.Farmer import Farmer
from src.grid import Grid
import time


def main():
    pigs = []
    for i in range(0,8,1):
        for j in range(1,3,2):
            for k in range(1,4,1):
                pig = Pig(j, k)
                pigs.append(pig)
    farmer = Farmer(1,0)

    grid = Grid(3,5)
    grid.putin(0,0,'O')

    running = True
    timeTaken = 0

    while running:

        grid.putin(farmer.x, farmer.y, 'F')

        for pig in pigs:
            for i in range(0, 3, 2):
                for j in range(1, 5):
                    grid.putin(i, j, pig.hunger)
            pig.getHungry()
            if pig.isStarving() and farmer.y == pig.y and farmer.capacity > 0:
                pig.hunger = 100

        grid.printgrid()
        print("")
        time.sleep(1)
        timeTaken += 1

        if timeTaken == 10:
            running = False



if __name__ == "__main__":
    main()
