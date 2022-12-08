import itertools
import sys
from os import path, getcwd

def part_1():
    count = 0
    with open(path.join(getcwd(), "4_input.txt"), "r") as f:
        for line in f:
            p = [x.split("-") for x in line.rstrip().split(",")]
            if int(p[0][0]) <= int(p[1][0]) and int(p[0][1]) >= int(p[1][1]) or \
                int(p[1][0]) <= int(p[0][0]) and int(p[1][1]) >= int(p[0][1]):
                count += 1
    return count


def part_2():
    count = 0
    with open(path.join(getcwd(), "4_input.txt"), "r") as f:
        for line in f:
            p = [(int(y[0]), int(y[1])) for y in [x.split("-") for x in line.rstrip().split(",")]]
            if p[0][0] <= p[1][0] and p[0][1] >= p[1][0] or \
                p[1][0] <= p[0][0] and p[1][1] >= p[0][0]:
                count += 1
    return count


if __name__ == "__main__":
    print(part_2())