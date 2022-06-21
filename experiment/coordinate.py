import random


def generate_number(min_value: float = 0.1, max_value: float = 0.9):
    return random.random() * (max_value - min_value) + min_value


def random_coordinate(min_value: float = 0.1, max_value: float = 0.9):
    return (generate_number(min_value, max_value),
            generate_number(min_value, max_value))

