import random


class Pig(object):

    def __init__(self, x, y):
        self.hunger = 100
        self.x = x
        self.y = y
        self.hungry = False

    def isStarving(self):
        if self.hunger < 50:
            self.hungry = True

    def getHungry(self):
        self.hunger = self.hunger - random.randrange(0, 5, 1)

