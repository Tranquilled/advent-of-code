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
    nums = []
    with open(path.join(getcwd(), "20_input.txt"), "r") as f:
        for line in f:
            nums.append(int(line.strip()))
    multiples = list(filter(lambda x: nums.count(x) > 1, nums))
    # print(len(multiples))  # there are many duplicates
    return tuple(nums)

Move = collections.namedtuple("Move", ["i", "v"])
    

def part_1(nums):
    mod = len(nums)
    moves = [Move(i, v) for i, v in enumerate(nums)]
    copy = [x for x in moves]
    
    for move in moves:
        # print(move)
        v = move.v
        idx = copy.index(move)
        dest = (idx + v) % (mod-1)  # omfg mod - 1
        # print(dest, v)
        copy.remove(move)
        # del copy(idx)
        copy.insert(dest if dest != 0 else mod, move)
        # print([m.v for m in copy])

    # print(len(moves))
    i_0 = [m.v for m in copy].index(0)
    print(i_0)
    print((i_0 + 1000) % mod, (i_0 + 2000) % mod, (i_0 + 3000) % mod)
    return copy[(i_0 + 1000) % mod].v + copy[(i_0 + 2000) % mod].v + copy[(i_0 + 3000) % mod].v


def part_2(nums):
    mod = len(nums)
    moves = [Move(i, v * 811589153) for i, v in enumerate(nums)]
    copy = [x for x in moves]
    
    for move in moves * 10:
        # print(move)
        v = move.v
        idx = copy.index(move)
        dest = (idx + v) % (mod-1)
        copy.remove(move)
        copy.insert(dest if dest != 0 else mod, move)


    i_0 = [m.v for m in copy].index(0)
    print(i_0)
    print((i_0 + 1000) % mod, (i_0 + 2000) % mod, (i_0 + 3000) % mod)
    print(copy[(i_0 + 1000) % mod].v, copy[(i_0 + 2000) % mod].v, copy[(i_0 + 3000) % mod].v)
    return copy[(i_0 + 1000) % mod].v + copy[(i_0 + 2000) % mod].v + copy[(i_0 + 3000) % mod].v


if __name__ == "__main__":
    x = input()
    # x = (1,2,-3,3,-2,0,4)
    # print(len(x))
    # print(part_1(x))
    # print("answer:", part_1(x))
    print("answer:", part_2(x))
