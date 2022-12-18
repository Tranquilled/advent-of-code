import collections
import inspect
import re
import sys
from functools import reduce
from itertools import product
from math import floor
from operator import itemgetter
from os import path, getcwd


def input():
    map = set()
    parse = r"(\d+),(\d+),(\d+)"
    with open(path.join(getcwd(), "18_input.txt"), "r") as f:
        for line in f:
            map.add(tuple(int(x) for x in re.findall(parse, line)[0]))
    return map


def part_1(map):
    faces = 6 * len(map)
    sides_seen = set()
    for cube in map:
        x, y, z = cube
        for side in [(x,y,z-1), (x,y,z+1), (x,y-1,z), (x,y+1,z), (x-1,y,z), (x+1,y,z)]:
            if side in sides_seen: faces -= 2
        sides_seen.add(cube)
    
    return faces


def neighbors(cube):
    x, y, z = cube
    return [(x,y,z-1), (x,y,z+1), (x,y-1,z), (x,y+1,z), (x-1,y,z), (x+1,y,z)]


def part_2(map):
    max_coords  = tuple(max(x[n] for x in map) + 1 for n in range(3))  # checked, min is 0
    # fill from (0,0,0)
    next = neighbors((0, 0, 0))
    seen = set()
    faces = 0
    while next:
        print(len(next))
        n = next.pop(0)
        if not(n in seen
               or any(a > b for a,b in zip(n, max_coords))
               or any(a < b for a,b in zip(n, (-1,-1,-1)))):
            seen.add(n)
            for neighbor in neighbors(n):
                if neighbor in map: faces += 1
                else: next.append(neighbor)
    return faces



if __name__ == "__main__":
    x = input()
    # print(part_1(x))
    print(part_2(x))