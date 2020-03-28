class Farmer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.capacity = 3

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
