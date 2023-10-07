import random
from abc import ABC, abstractmethod

from experimentation.entity import Entity


class Robot(ABC, Entity):

    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.collected = 0

    @abstractmethod
    def move(self):
        pass

    def eat(self):
        self.collected += 1

    def alive(self):
        return True

    def __repr__(self):
        return str(super().__repr__()) + " (" + str(self.collected) + ")"


class RandomRobot(Robot):
    def move(self):
        self.x += random.random() - 0.5
        self.y += random.random() - 0.5


class HungryRobot(Robot):
    def __init__(self, x: float, y: float, consumption: float = 0.05):
        super().__init__(x, y)
        self.food = 1.0
        self.consumption = consumption

    def move(self):
        if not self.alive():
            return
        super().move()
        self.food -= self.consumption

    def alive(self):
        return self.food > 0.0
