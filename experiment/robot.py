from experiment.coordinate import random_coordinate


class Robot:

    def __init__(self):
        self.x, self.y = random_coordinate()

    def move(self, forward: float, right: float):
        self.x += forward
        self.y += right

    def position(self):
        return self.x, self.y
