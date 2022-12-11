import collections
import inspect
import re
import sys
from math import floor
from operator import itemgetter
from os import path, getcwd

monkeys = [
    {
    "items": [59, 65, 86, 56, 74, 57, 56],
    "operation": lambda x: x * 17,
    "test": lambda x: x % 3 == 0,
    "true": lambda a, x: a[3]["items"].append(x),
    "false": lambda a, x: a[6]["items"].append(x)
    }, {
    "items": [63, 83, 50, 63, 56],
    "operation": lambda x: x + 2,
    "test": lambda x: x % 13 == 0,
    "true": lambda a, x: a[3]["items"].append(x),
    "false": lambda a, x: a[0]["items"].append(x)
    }, {
    "items": [93, 79, 74, 55],
    "operation": lambda x: x + 1,
    "test": lambda x: x % 2 == 0,
    "true": lambda a, x: a[0]["items"].append(x),
    "false": lambda a, x: a[1]["items"].append(x)
    }, {
    "items": [86, 61, 67, 88, 94, 69, 56, 91],
    "operation": lambda x: x + 7,
    "test": lambda x: x % 11 == 0,
    "true": lambda a, x: a[6]["items"].append(x),
    "false": lambda a, x: a[7]["items"].append(x)
    }, {
    "items": [76, 50, 51],
    "operation": lambda x: x ** 2,
    "test": lambda x: x % 19 == 0,
    "true": lambda a, x: a[2]["items"].append(x),
    "false": lambda a, x: a[5]["items"].append(x)
    }, {
    "items": [77, 76],
    "operation": lambda x: x + 8,
    "test": lambda x: x % 17 == 0,
    "true": lambda a, x: a[2]["items"].append(x),
    "false": lambda a, x: a[1]["items"].append(x)
    }, {
    "items": [74],
    "operation": lambda x: x * 2,
    "test": lambda x: x % 5 == 0,
    "true": lambda a, x: a[4]["items"].append(x),
    "false": lambda a, x: a[7]["items"].append(x)
    }, {
    "items": [86, 85, 52, 86, 91, 95],
    "operation": lambda x: x + 6,
    "test": lambda x: x % 7 == 0,
    "true": lambda a, x: a[4]["items"].append(x),
    "false": lambda a, x: a[5]["items"].append(x)
    }
]


def input():
    monkeys = [{
        "items": [],
        "operation": None,
        "test": None,
        "true": None,
        "false": None} for _ in range(8)]
    with open(path.join(getcwd(), "11_input.txt"), "r") as f:
        i = 0
        for line in f:
            if line == "\n":
                i += 1
                continue
            l = line.strip()
            if "Starting items" in l:
                monkeys[i]["items"] = [int(n) for n in l.split(": ")[1].split(", ")]
            if "Operation" in l:
                n = re.search(r"new = (.+)$", l)
                op = n.group(1)
                monkeys[i]["operation"] = eval("lambda old: " + op)
            if "Test" in l:
                n = re.search(r"(\d+)", l)
                monkeys[i]["test"] = eval(f"lambda x: x % {n.group(1)} == 0")
            if "If true" in l:
                n = re.search(r"(\d+)", l)
                monkeys[i]["true"] = eval(f'lambda a, x: a[{n.group(1)}]["items"].append(x)')
            if "If false" in l:
                n = re.search(r"(\d+)", l)
                monkeys[i]["false"] = eval(f'lambda a, x: a[{n.group(1)}]["items"].append(x)')
    return monkeys


def part_1(monkeys):
    round = 1
    m = 0
    activity = [0 for _ in range(len(monkeys))]
    while round < 21:
        monkey = monkeys[m]
        items = monkey["items"]
        while len(items) > 0:
            i = items.pop(0)
            # inspect, get bored
            i = floor(monkey["operation"](i) / 3)
            activity[m] += 1
            # test
            # print(m, "test")
            if monkey["test"](i):
                # print(m, "true")
                monkey["true"](monkeys, i)
            else:
                # print(m, i, "false")
                monkey["false"](monkeys, i)
        if m == len(monkeys) - 1:
            m = 0
            round += 1
        else:
            m += 1
            monkey = monkeys[m]
            items = monkey["items"]
        # print("\n".join(str(i["items"]) for i in monkeys))
    # return "\n".join(str(i["items"]) for i in monkeys)
    return sorted(activity)
    # activity = [len(i["items"])]


def part_2(monkeys):
    round = 1
    m = 0
    activity = [0 for _ in range(len(monkeys))]
    while round < 10001:
        monkey = monkeys[m]
        items = monkey["items"]
        while len(items) > 0:
            i = items.pop(0)
            # inspect, get bored
            i = monkey["operation"](i)
            activity[m] += 1
            # reduce
            i = i % 9699690  # divisibility test numbers were 3, 13, 2, 11, 19, 17, 5, 7
            # test
            if monkey["test"](i):
                monkey["true"](monkeys, i)
            else:
                monkey["false"](monkeys, i)
        if m == len(monkeys) - 1:
            m = 0
            round += 1
            print(round, list(len(i["items"]) for i in monkeys))
        else:
            m += 1
            monkey = monkeys[m]
            items = monkey["items"]
    print(sorted(activity))
    return sorted(activity)[-1] * sorted(activity)[-2]

if __name__ == "__main__":
    # print(input())
    # print(part_1(monkeys))
    print(part_1(input()))
    # print(part_2(monkeys))