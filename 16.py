import collections
import functools
import inspect
import re
import sys
from itertools import product, permutations
from math import floor
from operator import itemgetter
from os import path, getcwd


def input():
    valves = dict()
    parse = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels* leads* to valves* ([A-Z, ]+)")
    with open(path.join(getcwd(), "16_input.txt"), "r") as f:
        for line in f:
            d = re.match(parse, line.strip())
            valves[d.group(1)] = {
                "r": int(d.group(2)),
                "t": d.group(3).split(", "),
            }
    return valves


def web(valves, start, dest):
    # shortest = dict()
    if dest in (ts := valves[start]["t"]):
        return 1
    paths = [[t] for t in ts]
    while len(paths) > 0:
        p = paths.pop(0)
        for t in valves[p[-1]]["t"]:
            if t == dest:
                # print(p + [t])
                return len(p) + 1
            if t not in [x[-1] for x in paths]:
                paths.append(p + [t])


def part_1(v, used=set(), start=30):
    # most valves have r = 0, so they're not worth opening
    targets = sorted([k for k, a in v.items() if a["r"] > 0 and k not in used], key= lambda x:v[x]["r"])
    # print(used)
    results = set()
    paths_seen = dict() # avoid running web
    next = []
    for x in targets:
        paths_seen["AA" + x] = (p := web(v, "AA", x))
        next.append({
                     "v": x, # name of valve
                     "t_r": start - p, # time remaining
                     "f": 0, # flow
                     "s": {x} # targets seen
                    })
    while len(next) > 0:
        # BFS only works because targets is sorted
        n, t_r, f, s = itemgetter("v", "t_r", "f", "s")(next.pop(0))
        # TODO: Why does BFS terminate so much sooner than DFS?
        r = v[n]["r"]
        t_r -= 1
        f += t_r * r
        # print(" ".join(s), f, t_r)
        for dest in targets:
            try:
                p = paths_seen[n+dest]
            except KeyError:
                p = web(v, n, dest)
            if (t := t_r - p) < 1: # if t < 1 I can't turn the valve anyway
                # if f not in results:
                results.add(f)
            elif dest not in s and all(f >= x["f"] for x in next):
                next.append({
                    "v": dest,
                    "t_r": t,
                    "f": f,
                    "s": s | {dest}
                })
    return max(results)
    # return (r := sorted(results, key=lambda x: x["f"])), \
    #         (best := r[-1]["f"]), [set(n["s"]) for n in r if n["f"] >= best]

v = input()
@functools.cache
def naive_walk(current="AA", time=30, open=frozenset()):
    if time < 1:
        return 0
    loc = v[current]
    # for i in loc["t"]:
    score = max([naive_walk(i, time - 1, open) for i in loc["t"]])
    if loc["r"] > 0 and current not in open and time > 0:
        time -= 1
        points = loc["r"] * time
        open = open | {current}
        for i in loc["t"]:
            score = max(score, points + naive_walk(i, time-1, open))
    return score

@functools.cache
def naive_walk_2(current="AA", time=26, open=frozenset()):
    if time < 1:
        return naive_walk(time=26, open=open)
    loc = v[current]
    score = max([naive_walk_2(i, time - 1, open) for i in loc["t"]])
    if loc["r"] > 0 and current not in open and time > 0:
        time -= 1
        points = loc["r"] * time
        open = open | {current}
        for i in loc["t"]:
            score = max(score, points + naive_walk_2(i, time-1, open))
    return score
    

if __name__ == "__main__":
    x = input()
    # print(sum([a["r"] for a in x.values() if a["r"] > 0]))  # max flow is 214
    # print([a["r"] for a in x.values() if a["r"] > 0])  # 15 nonzero valves
    # print(web(x, "YX", "RS"))
    print(part_1(x))
    # print(part_2(x, start=26))
    print(naive_walk_2())