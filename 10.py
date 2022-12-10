import collections
import re
import sys
from math import floor
from operator import itemgetter
from os import path, getcwd


def check(x, cycle):
    if cycle % 40 == 20:
        return x * cycle
    return 0

def part_1():
    x = 1
    cycle = 0
    strength = 0
    with open(path.join(getcwd(), "10_input.txt"), "r") as f:
        for line in f:
            cycle += 1
            strength += check(x, cycle)
            if "addx" in line:
                cycle += 1
                strength += check(x, cycle)
                _, n = line.rstrip().split(" ")
                x += int(n)
    return strength


def draw(cycle, image, x):
    row = floor((cycle - 1) / 40)
    i = (cycle - 1) % 40
    # if x - 1 <= cycle % 40 <= x + 1: print(cycle, (row, i), x)
    # image[floor((cycle-1)/40)][(cycle-1) % 40] = f"{cycle} " # 
    image[row][i] = "#" if x - 1 <= i <= x + 1 else " "
    return image

def part_2():
    x = 1
    cycle = 0
    image = [["_"] * 40 for x in range(6)]
    with open(path.join(getcwd(), "10_input.txt"), "r") as f:
        for line in f:
            cycle += 1
            image = draw(cycle, image, x)
            # cycle += 1
            # image[cycle] = "#" if x - 1 <= cycle <= x + 1 else "."
            if "addx" in line:
                cycle += 1
                image = draw(cycle, image, x)
                _, n = line.rstrip().split(" ")
                x += int(n)
    image = ["".join(x) for x in image]
    return "\n".join(image)
    # return "\n".join(image[i:i+40] for i in range(0, 240, 40))


if __name__ == "__main__":
    print(part_1())
    print(part_2())