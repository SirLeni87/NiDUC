from builtins import print
import math

from src.Pig import Pig
from src.Farmer import Farmer
from src.grid import Grid


def main():
    pigs = []
    averageStarveTimeForOne = []
    averageWaitTimeForOne = []
    savedTime = []

    for i in range(8):
        averageStarveTimeForOne.append(0)
        averageWaitTimeForOne.append(0)
        savedTime.append([])

    print("Available farmer's strategies are: \n"
          "1 - Farmer prioritizes pigs that are the most hungry \n"
          "2 - Farmer prioritizes hungry pigs that are closer to him \n")

    strategy = int(input("What is your prefered farmer strategy? \n"))

    running = int(input("How many loops you want the simulation to take? \n"))

    fileName = (input("The file to save data in: "))
    saveFile = open(fileName, "w+")

    print("")
    starveTimeTotal = 0

    for a in range(100):
        for j in range(0, 3, 2):
            for k in range(1, 11, 1):
                pig = Pig(j, k)
                pigs.append(pig)
        farmer = Farmer(1, 0)

        grid = Grid(3, 11)

        timeTaken = 0
        for z in range(running):
            farmer.targets(pigs, strategy)
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
            timeTaken += 1

            farmer.lastY = farmer.y
            farmer.lastX = farmer.x

        starveTime = 0

        index = 0
        for pig in pigs:
            savedTime[index].append(pig.counter)
            starveTime += pig.counter
            averageStarveTimeForOne[index] += pig.counter
            averageWaitTimeForOne[index] += (pig.timehungry/pig.timeshungry)
            index += 1

        pigs.clear()
        for pig in pigs:
            del pig
        del farmer
        del grid

    for i in range(len(averageStarveTimeForOne)):
        starveTimeTotal += averageStarveTimeForOne[i]
    starveTimeTotal = starveTimeTotal/800

    resultTab = []
    for i in range(len(averageStarveTimeForOne)):
        result = 0
        for j in range(100):
            result += pow((savedTime[i][j] - (averageStarveTimeForOne[i]/100)), 2)
        result = math.sqrt(result/100)
        resultTab.append(result)

#----------------------------------------- MODEL --------------------------------------------



    saveFile.write("\n\n\n============================== TO_EXCEL ==============================\n")
    for i in range(8):
        saveFile.write("Pig " + str("%d\n" % i))
        for j in range(100):
            saveFile.write(str("%.2f\n" % savedTime[i][j]))
        saveFile.write("\n")

    saveFile.write("\n\n\n============================== TO_EXCEL ==============================\n")

    saveFile.write("\n\n\n============================== SUMMARY ==============================\n")
    saveFile.write("Total average starve time: " + str(starveTimeTotal))

    for i in range(len(averageStarveTimeForOne)):
        saveFile.write("\nPig[" + str(i) + "] was on average:   starving for: " + str("%.2f" % (averageStarveTimeForOne[i]/100)) + "    hungry for: " + str("%.2f" % (averageWaitTimeForOne[i]/100)))

    saveFile.write("\n\nStandard deviation for starve time:")

    for i in range(len(resultTab)):
        saveFile.write("\nPig[" + str(i) + "]: " + str(resultTab[i]))

    saveFile.close()

    print("DONE")

if __name__ == "__main__":
    main()
