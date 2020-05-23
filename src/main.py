from builtins import print

from src.Pig import Pig
from src.Farmer import Farmer
from src.grid import Grid


def main():
    pigs = []
    averageStarveTimeForOne = []
    averageWaitTimeForOne = []

    for i in range(8):
        averageStarveTimeForOne.append(0)
        averageWaitTimeForOne.append(0)

    # for j in range(0,3,2):
    #     for k in range(1,5,1):
    #         pig = Pig(j, k)
    #         pigs.append(pig)
    # farmer = Farmer(1,0)

    # grid = Grid(3,5)
    # grid.putin(0,0,'O')

    print("Available farmer's strategies are: \n"
          "1 - Farmer prioritizes pigs that are the most hungry \n"
          "2 - Farmer prioritizes hungry pigs that are closer to him \n")

    strategy = int(input("What is your prefered farmer strategy? \n"))

    running = int(input("How many loops you want the simulation to take? \n"))

    fileName = (input("The file to save data in: "))
    saveFile = open(fileName, "w+")

    print("")
    # timeTaken = 0
    starveTimeTotal = 0

    for a in range(100):
        for j in range(0, 3, 2):
            for k in range(1, 5, 1):
                pig = Pig(j, k)
                pigs.append(pig)
        farmer = Farmer(1, 0)

        grid = Grid(3, 5)
        # grid.putin(0, 0, 'O')

        timeTaken = 0
        for z in range(running):
            farmer.targets(pigs, strategy)
            # print(str(farmer.targetX) + "," + str(farmer.targetY))
            farmer.move()

            grid.putin(farmer.lastX, farmer.lastY, '.')

            grid.putin(farmer.x, farmer.y, 'F')

            for pig in pigs:
                pig.getHungry()
                pig.isHungry()
                grid.putin(pig.x, pig.y, pig.hunger)
                if farmer.targetX == pig.x and farmer.targetY == pig.y and farmer.y == pig.y and farmer.capacity > 0:
                    pig.hunger = 100
                    pig.hungry = False
                    farmer.feed()

            # print("Food capacity: ", end = '')
            # for i in range(farmer.capacity):
                # print("*", end = '')
            # print("")
            # grid.printgrid()
            # print("")
            # time.sleep(1)
            timeTaken += 1

            farmer.lastY = farmer.y
            farmer.lastX = farmer.x

        starveTime = 0
        # for pig in pigs:
        #     starveTime += pig.counter
        #     print("pig at [" + str(pig.x) + "," + str(pig.y)+"] was starving for " + str(pig.counter) + " time units and waiting for average " + str(pig.timehungry/pig.timeshungry))

        # print("Total time of pigs starving: " + str(starveTime) + " time units.")

        index = 0
        for pig in pigs:
            starveTime += pig.counter
            averageStarveTimeForOne[index] += pig.counter
            averageWaitTimeForOne[index] += (pig.timehungry/pig.timeshungry)
            index += 1
            saveFile.write("pig at [" + str(pig.x) + "," + str(pig.y)+"] was starving for " + str(pig.counter) + " time units and waiting for average " + str("%.2f" % (pig.timehungry/pig.timeshungry)) + "\n")

        saveFile.write("\n" + "Total time of pigs starving: " + str(starveTime) + " time units. \n\n\n")
        starveTimeTotal += starveTime

        pigs.clear()
        for pig in pigs:
            del pig
        del farmer
        del grid

    saveFile.write("\n\n\n============================== SUMMARY ==============================\n")
    saveFile.write("Simulation's average total starve time: " + str(starveTimeTotal/100))

    for i in range(len(averageStarveTimeForOne)):
        saveFile.write("\nPig[" + str(i) + "] was on average:   starving for: " + str("%.2f" % (averageStarveTimeForOne[i]/100)) + "    hungry for: " + str("%.2f" % (averageWaitTimeForOne[i]/100)))


    saveFile.close()

    print("DONE")

if __name__ == "__main__":
    main()
