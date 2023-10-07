import random


class Environment:

    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def random_coordinate(self) -> (float, float):
        x = random.uniform(-self.width / 2, self.width / 2)
        y = random.uniform(-self.height / 2, self.height / 2)
        return x, y
