import math


class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return self.x, self.y

    def distance(self, other: 'Entity'):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return str(self.__class__.__name__) + " [" + str(round(self.x, 1)) + ", " + str(round(self.y, 1)) + "]"
