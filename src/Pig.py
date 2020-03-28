

class Pig():

    def __init__(self, hunger = 100, x = 0, y = 0, hungry = False):
        self.hunger = hunger
        self.x = x
        self.y = y
        self.hungry = hungry

    def isStarving(self):
        if self.hunger < 50:
            self.hungry = True

    def getFed(self):
        print("TODO")

