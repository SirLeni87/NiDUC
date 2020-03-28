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
    farmer = Farmer(3,0)

    grid = Grid(3,5)
    grid.putin(0,0,'O')
    grid.putin(0,1,'F')
    for i in range(0,3,2):
        for j in range(1,5):
            grid.putin(j,i,'P')

    running = True

    while running:
        grid.printgrid()
        time.sleep(1)
        running = False



if __name__ == "__main__":
    main()
