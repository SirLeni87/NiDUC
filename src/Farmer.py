class Farmer(object):
    def __init__(self, x, y):
        self.lastX = x
        self.lastY = y
        self.x = x
        self.y = y
        self.capacity = 3
        self.state = 0
        self.targetY= 0
        self.targetX= 0

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getCapacity(self):
            return self.y

    def setCapacity(self, capacity):
            self.capacity = capacity

    def pickFood(self):
        self.capacity = 3 #later add parametr with amount of food to pick up

    def feed(self):
        self.capacity = self.capacity-1
    def targets(self, pigs, strategy):
        if self.state == 0:
            if self.capacity == 0:
                self.targetX = 0
                self.targetY = 0
                self.state = 1
            else:
                minimum = 51
                for pig in pigs:

                    if pig.hungry and pig.hunger < minimum:
                        minimum = pig.hunger
                        self.targetY = pig.y
                        self.targetX = pig.x
                        self.state = 2

    def move(self):
        if self.state == 1:
            self.y -= 1
            if self.targetY == self.y:
                self.pickFood()
                self.state = 0
        elif self.state == 2:
            if self.y == self.targetY:
                self.state = 0
            elif self.y > self.targetY:
                self.y -= 1
                if self.y == self.targetY:
                    self.state = 0
            else:
                self.y += 1
                if self.y == self.targetY:
                    self.state = 0





