from typing import Type

from experimentation.entity import Entity
from experimentation.environment import Environment
from experimentation.food import FoodPellet
from experimentation.robot import Robot


class EntityFactory:

    def __init__(self, environment: Environment):
        self.environment: Environment = environment

    def create(self, entity: Type[Entity]):
        x, y = self.environment.random_coordinate()
        return entity(x, y)


if __name__ == "__main__":
    e = Environment(10, 10)
    ef = EntityFactory(e)
    print(ef.create(Robot))
    print(ef.create(FoodPellet))
