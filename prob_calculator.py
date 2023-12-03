import copy
import random
from unittest import main


class Hat:
    def __init__(self, **kwargs):
        """
        Take in a variable number of arguments that specific the number of balls of each color in a hat.
        Convert those to a list of string with one item for each ball of that color.
        """
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)

    def draw(self, number):
        """
        Indicate the number of balls to draw from the hat.
        Remove the balls at random and return them as a list of strings.
        """
        number = min(number, len(self.contents))
        draw = [self.contents.pop(random.randrange(len(self.contents))) for _ in range(number)]
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Take in the testing information (i.e. group of balls to draw, number of balls drawn, and number of experiments.)
    """
    z = 0
    for _ in range(num_experiments):
        hat_b = copy.deepcopy(hat)
        balls_drawn = hat_b.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        z += 1 if balls_req == len(expected_balls) else 0

    return z / num_experiments