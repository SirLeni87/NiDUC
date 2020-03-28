class Grid(object):
    def __init__(self, x, y):
        self.xsize = x
        self.ysize = y
        self.siatka = []
        for i in range(y):
            self.siatka.append([])
        i = 0
        for i in range(x):
            for j in range(y):
                self.siatka[j].append('.')

    def gety(self):
        return self.ysize

    def getx(self):
        return self.xsize

    def putin(self, x, y, c):
        self.siatka[x][y] = c

    def getelement(self, x, y):
        return self.siatka[x][y]

    def printgrid(self):
        for i in range(self.ysize):
            print(self.siatka[i])


