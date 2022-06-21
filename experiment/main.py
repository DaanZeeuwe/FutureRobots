import math

from matplotlib import pyplot as plt

from experiment.coordinate import random_coordinate
from experiment.robot import Robot

if __name__ == "__main__":
    food = [random_coordinate() for _ in range(25)]
    food_eaten = []
    water = [random_coordinate() for _ in range(5)]
    robot: Robot = Robot()
    min_distance = (0.2) ** 2

    for i in range(1000):
        movement = random_coordinate()
        robot.move((movement[0] - 0.5) / 10, (movement[1] - 0.5) / 10)
        x1, y1 = robot.position()
        distance = []
        for x2, y2 in food:
            distance.append(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

        removed = []
        for i, d in enumerate(distance):
            if d <= min_distance:
                removed.append(i)

        removed = reversed(removed)

        for remove_index in removed:
            element = food.pop(remove_index)
            food_eaten.append(element)

    fig, ax = plt.subplots()
    for x, y in food:
        ax.plot(x, y, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")  # A tuple unpacking to unpack the only plot

    for x, y in food_eaten:
        ax.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="red")  # A tuple unpacking to unpack the only plot

    x, y = robot.position()
    plt.plot(x, y, marker="o", markersize=15, markeredgecolor="black", markerfacecolor="grey")
    print("last robot", x, y)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.show()