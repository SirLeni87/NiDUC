from src.Pig import Pig
from src.Farmer import Farmer
from src.grid import Grid
import time


def main():
    pigs = []
    for j in range(0,3,2):
        for k in range(1,5,1):
            pig = Pig(j, k)
            pigs.append(pig)
    farmer = Farmer(1,0)

    grid = Grid(3,5)
    grid.putin(0,0,'O')

    running = int(input("How many loops you want the simulation to take? \n"))
    timeTaken = 0

    print("")

    for z in range(running):

        farmer.targets(pigs)
        print(str(farmer.targetX) + "," + str(farmer.targetY))
        farmer.move()

        grid.putin(farmer.lastX, farmer.lastY, '.')

        grid.putin(farmer.x, farmer.y, 'F')

        for pig in pigs:
            pig.getHungry()
            pig.isStarving()
            grid.putin(pig.x, pig.y, pig.hunger)
            if farmer.targetX == pig.x and farmer.targetY == pig.y and farmer.y == pig.y and farmer.capacity > 0:
                pig.hunger = 100
                pig.hungry = False
                farmer.feed()

        print("Food capacity: ", end = '')
        for i in range(farmer.capacity):
            print("*", end = '')
        print("")
        grid.printgrid()
        print("")
        time.sleep(1)
        timeTaken += 1

        farmer.lastY = farmer.y
        farmer.lastX = farmer.x

    starveTime = 0
    for pig in pigs:
        starveTime += pig.counter
        print("pig at [" + str(pig.x) +"," + str(pig.y)+"] was starving for " + str(pig.counter) + " time units and waiting for average " + str(pig.timehungry/pig.timeshungry))

    print("Total time of pigs starving: " + str(starveTime) + " time units.")



if __name__ == "__main__":
    main()
