import collections
import inspect
import re
import sys
from functools import cmp_to_key
from itertools import zip_longest
from math import floor
from operator import itemgetter
from os import path, getcwd


def input():
    packets = []
    with open(path.join(getcwd(), "13_input.py"), "r") as f:
        pair = []
        for line in f:
            if line.strip() == "":
                packets.append(pair)
                pair = []
                continue
            pair.append(eval(line.strip()))
    return packets


def good(l, r):
    # print(f"parent:\n {left} \n {right}")
        # print(f"child:\n {l} \n {r}")
        # if l is None: return True
        # if r is None: return False
    if type(l) == int and type(r) == int:
        if l == r: return None
        return l < r
    if type(l) == list and type(r) == list:
        # If the right list runs out of items first, the inputs are not in the right order. ??
        # if len(l) > len(r): return False
        # if len(l) < len(r): continue
        # if not good(l, r): return False
        for a, b in zip(l,r):
            x = good(a,b)
            if x is not None: return x
        return good(len(l), len(r))
    if type(l) == int and type(r) == list:
        # if not good([l], r): return False
        return good([l], r)
    if type(l) == list and type(r) == int:
        # if not good(l, [r]): return False
        return good(l, [r])


def pairwise(l,r):
    if good(l,r) == None: return 0
    elif good(l,r): return -1
    return 1


def part_1(packets):
    good_pairs = list()
    for i, pair in enumerate(packets):
        l, r = itemgetter(0,1)(pair)
        if good(l, r): 
            good_pairs.append(i + 1)
    print(good_pairs)
    return sum(good_pairs)


def part_2(packets):
    compare = cmp_to_key(pairwise)

    packets = sorted(packets, key=compare)
    # print("\n".join([str(x) for x in packets]))
    print(packets.index([[2]]), packets.index([[6]]))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    x = input()
    # print(part_1(x))
    x = [b for a in x for b in a]
    x.append([[2]])
    x.append([[6]])
    print(part_2(x))