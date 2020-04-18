import random
import time


class Pig(object):

    def __init__(self, x, y):
        self.hunger = 100
        self.x = x
        self.y = y
        self.hungry = False
        self.counter = 0
        self.timehungry = 0
        self.timeshungry = 0


    def isHungry(self):
        if self.hunger < 50:
            self.hungry = True

    def getRandomNumber(self):
        random.seed(time.perf_counter())
        number = random.randint(0,5)
        return number

    def getHungry(self):
        if(self.hunger > 0):
            self.hunger = self.hunger - self.getRandomNumber()
        if self.hungry == False:
            self.isHungry()
            if self.hungry == True:
                self.timeshungry +=1

        if self.hunger < 50:
            self.timehungry += 1

        if self.hunger < 20:
            self.counter += 1

