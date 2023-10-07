import math
from typing import List, Tuple

import torch
from matplotlib import pyplot as plt

from controller import RobotController
from experimentation.coordinate import random_coordinate
from experimentation.robot import Robot

if __name__ == "__main__":
    food = [random_coordinate() for _ in range(25)]
    food_eaten = []
    water = [random_coordinate() for _ in range(5)]
    robot: Robot = Robot()
    min_distance = (0.2) ** 2

    trajectory: List[Tuple[float, float]] = []
    controller = RobotController()
    for parameter in controller.parameters():
        print(parameter)

    for i in range(100):

        x1, y1 = robot.position()
        trajectory.append((x1, y1))
        distance = []
        observation = [0.0 for _ in range(8)]

        for x2, y2 in food:
            angle = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
            index = math.floor(angle / 180 * 4 + 4)
            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            # math.sqrt(2) = max distance in the area, making it a maximization problem.
            max_length = math.sqrt(2)
            # the smaller the distance to the object, the stronger the signal becomes.
            if (max_length - d) > observation[index]:
                observation[index] = max_length - d
            distance.append(d)

        # Food Cleanup
        removed = []
        for i, d in enumerate(distance):
            if d <= min_distance:
                removed.append(i)
        removed = reversed(removed)
        for remove_index in removed:
            element = food.pop(remove_index)
            food_eaten.append(element)
            distance.pop(remove_index)

        movement = random_coordinate()
        move = controller.forward(torch.tensor(observation)).detach()
        robot.move((move[0] - 0.5) / 25, (move[1] - 0.5) / 25)

    fig, ax = plt.subplots()
    for x, y in food:
        ax.plot(x, y, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")  # A tuple unpacking to unpack the only plot

    for x, y in food_eaten:
        ax.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="red")  # A tuple unpacking to unpack the only plot

    for x, y in trajectory:
        ax.plot(x, y, marker="o", markersize=1, markeredgecolor="blue", markerfacecolor="red")  # A tuple unpacking to unpack the only plot

    x, y = robot.position()
    plt.plot(x, y, marker="o", markersize=15, markeredgecolor="black", markerfacecolor="grey")
    print(len(food_eaten))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.show()