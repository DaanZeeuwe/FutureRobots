from typing import List

from experimentation.environment import Environment
from experimentation.factory import EntityFactory
from experimentation.food import FoodPellet
from experimentation.robot import Robot, RandomRobot

food_threshold = 1

class Experiment:

    def __init__(self, environment: Environment, robots: List[Robot], food_pellets: List[FoodPellet]):
        self.environment: Environment = environment
        self.robots: List[Robot] = robots
        self.food_pellets: List[FoodPellet] = food_pellets

    def step(self):
        for robot in self.robots:
            robot.move()
            eaten = any(robot.distance(food) < food_threshold for food in self.food_pellets)
            if eaten:
                self.food_pellets = [food for food in self.food_pellets if robot.distance(food) >= food_threshold]
                robot.eat()
        print("food left", len(self.food_pellets))


class ExperimentFactory:

    def __init__(self, environment: Environment = Environment(10, 10)):
        self.environment = environment
        self.factory = EntityFactory(environment)

    def create(self, robots: int = 5, food_pellets: int = 25):
        robots = [self.factory.create(RandomRobot) for _ in range(robots)]
        food_pellets = [self.factory.create(FoodPellet) for _ in range(food_pellets)]
        return Experiment(self.environment, robots, food_pellets)
