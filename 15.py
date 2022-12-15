import collections
import inspect
import re
import sys
from itertools import product
from math import floor
from operator import itemgetter
from os import path, getcwd


def input():
    pairs = []
    parse = r"([\d-]+)"
    with open(path.join(getcwd(), "15_input.txt"), "r") as f:
        for line in f:
            a, b, c, d = [int(x) for x in re.findall(parse, line.strip())]
            pairs.append({
                "s": complex(a, b),
                "b": complex(c, d),
                "dist": abs(a-c) + abs(b-d)
            })
    return pairs


def part_1(pairs):
    twomil = set(s.real for x in pairs for s in itemgetter("s", "b")(x) if s.imag == 2000000)
    print(twomil)  # the identified one is a beacon; subtract 1
    for p in pairs:
        s, d = itemgetter("s", "dist")(p)
        if (j := abs(2000000 - s.imag)) > d: continue
        r = d - j
        twomil.update(a for a in range(int(s.real - r), int(s.real + r + 1)))
    return len(twomil) - 1


# def rule_out(pairs, idx):
#     found = set(range(4000001))
#     while len(found) > 0:
#         for p in pairs:
#             s, d = itemgetter("s", "dist")(p)
#             if (j := abs(idx - s.imag)) > d: continue
#             r = d - j
#             found.difference_update(range(max(0, int(s.real - r)), min(4000001, int(s.real + r + 1))))
#         if len(found) == 1:
#             print(found,idx)
#             return found, idx
#     return False


# def dists(pairs):
#     dists = []
#     for p in pairs:
#         s, d = itemgetter("s", "dist")(p)
#         def x(idx, s=s, d=d):
#             if (j := abs(idx - s.imag)) > d: return range(0)
#             r = d - j
#             return range(max(0, int(s.real - r)), min(4000001, int(s.real + r + 1)))
#         dists.append(x)
#     return dists


# def search(funcs, idx):
#     # if there's a known beacon, it doesn't count
#     found = set(range(4000001))
#     for f in funcs:
#         found.difference_update(f(idx))
#         if len(found) == 0:
#             break

#     if len(found) == 1:
#         print(found, idx)
#         return found, idx
#     # print(f"{idx} didn't work out")
#     return False


# def part_2(pairs):
#     # there is guaranteed to be exactly 1 non-seen, non-S, non-B space
#     funcs = dists(pairs)
#     print(funcs, type(funcs[0]))
#     for idx in range(4000001):
#         if result := search(funcs, idx):
#             return result


def make_func(s, d):
    def f(x, y):
        # print(type(abs(int(s.real) - x)) , type(d))
        #  True: not the beacon. False: could be beacon
        return abs(int(s.real) - x) + abs(int(s.imag) - y) <= d
    return f


def eqs(pairs):
    eqs = []
    for p in pairs:
        s, d = itemgetter("s", "dist")(p)
        eqs.append(make_func(s,d))
    return eqs


def informed_part_2(pairs):
    # there is only 1 open point, so it must be exactly outside a sensor boundary
    fs = eqs(pairs)
    print(list(f(1, 0) for f in fs))
    for p in pairs:
        # borders = set()
        s, d = itemgetter("s", "dist")(p)
        x = int(s.real)
        y = int(s.imag)
        # borders.update(zip(range(x - d - 1, x + 1), range(y, y + d + 2)))
        # borders.update(zip(range(x, x + d + 2), range(y + d + 1, y - 1, -1)))
        # borders.update(zip(range(x + d + 1, x - 1, -1), range(y, y - d - 2, -1)))
        # borders.update(zip(range(x, x - d - 2, -1), range(y - d - 1, y + 1)))
        
        for n in zip(range(max(0, x - d - 1), min(4000001, x + 1)), range(max(0, y), min(4000001, y + d + 2))):
            evaluate(n, fs)
        for n in zip(range(max(0, x), min(4000001, x + d + 2)), range(min(4000001, y + d + 1), max(0, y - 1), -1)):
            evaluate(n, fs)
        for n in zip(range(min(4000001, x + d + 1), max(0, x - 1), -1), range(min(4000001, y), max(0, y - d - 2), -1)):
            evaluate(n, fs)
        for n in zip(range(min(4000001, x), max(0, x - d - 2), -1), range(max(0, y - d - 1), min(4000001, y + 1))):
            evaluate(n, fs)


def evaluate(b, fs):
    x, y = b
    if not any(f(x,y) for f in fs):
        print(x, y, 4000000 * x + y)


if __name__ == "__main__":
    x = input()
    # print(part_1(x))
    print(informed_part_2(x))