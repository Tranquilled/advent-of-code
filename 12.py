import collections
import inspect
import re
import sys
from math import floor
from operator import itemgetter
from os import path, getcwd


def input():
    map = []
    with open(path.join(getcwd(), "12_input.txt"), "r") as f:
        for line in f:
            map += [[]]
            map[-1] += [ord(x) for x in line.strip()]
    return map


def walk(cur, map):  # cur = Tuple<(int<e>, str<path>, List<[Tuple<(int, int)>]>)>
    e, path, hist, last = itemgetter("e", "path", "hist", "last")(cur)
    e += 1
    y, x = last
    for k, v in {(y - 1, x): "^",
                 (y + 1, x): "v",
                 (y, x - 1): "<",
                 (y, x + 1): ">"}.items():
        if k not in hist and 0 <= k[0] <= 40 and 0 <= k[1] <= 80 and map[k[0]][k[1]] <= e:
            yield {
                "e": map[k[0]][k[1]],
                "path": path + v, # always 1 shorter than hist
                "hist": hist | {k},
                "last": k
            }
def part_1(map):
    start = {
        "e": ord("a"),
        "path": "",
        "hist": {(20, 0)},
        "last": (20, 0)
      }  # from Ctrl + F
    paths = set()  # possible solutions
    steps = list(walk(start, map))  # stack of possible steps
    while len(steps) > 0:
        step = steps.pop(0)  # BFS; paths in queue are guaranteed to be shorter than new
        h = step["e"]
        if h == 69:  # ord("E")
            # paths.add(step[1])
            # continue
            return step, len(step["path"])
        # if h == 83:  # ord("S")
        #     continue
        for s in walk(step, map):
            if s["last"] not in set(x["last"] for x in steps):
                steps.append(s)
        print(len(paths), len(steps))
    print(paths)
    return min([len(x) for x in paths])


def fast_walk(cur, map):
    e, hist, last = itemgetter("e", "hist", "last")(cur)
    e -= 1
    y, x = last
    for k in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if k not in hist and 0 <= k[0] <= 40 and 0 <= k[1] <= 80 and map[k[0]][k[1]]  >= e:
            yield {
                "e": map[k[0]][k[1]],
                "hist": hist | {k},
                "last": k
            }

def part_2(map):
    start = {
        "e": ord("z"),
        "hist": {(20, 58)},
        "last": (20, 58)
      }  # from Ctrl + F
    steps = list(fast_walk(start, map))
    while len(steps) > 0:
        step = steps.pop(0)
        if step["e"] == 97 or step["e"] == 83:
            return step, len(step["hist"])
        for s in fast_walk(step, map):
            if s["last"] not in set(x["last"] for x in steps):
                steps.append(s)



if __name__ == "__main__":
    # x = input()
    # print(x)
    # print(x[20][58])
    # print(part_1(input()))
    print(part_2(input()))