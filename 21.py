import collections
import inspect
import re
import sympy
import sys
from functools import reduce
from itertools import product
from math import floor
from operator import itemgetter
from os import path, getcwd


def create_lambda(var1, op, var2):
    # print(var1, op, var2)
    if op == "+":
        return lambda d: d[var1] + d[var2]
    if op == "-":
        return lambda d: d[var1] - d[var2]
    if op == "*":
        return lambda d: d[var1] * d[var2]
    if op == "/":
        return lambda d: d[var1] / d[var2]

Node = collections.namedtuple("Node", ["func", "args"])

test_input = {
    "root": create_lambda("pppw", "+", "sjmn"),
    "dbpl": 5,
    "cczh": create_lambda("sllz", "+", "lgvd"),
    "zczc": 2,
    "ptdq": create_lambda("humn", "-", "dvpt"),
    "dvpt": 3,
    "lfqf": 4,
    "humn": 5,
    "ljgn": 2,
    "sjmn": create_lambda("drzm", "*", "dbpl"),
    "sllz": 4,
    "pppw": create_lambda("cczh", "/", "lfqf"),
    "lgvd": create_lambda("ljgn", "*", 'ptdq'),
    "drzm": create_lambda("hmdt", "-", "zczc"),
    "hmdt": 32
}

humn = sympy.symbols("humn")
print(type(humn))

test_tree = {
    "root": Node(lambda x,y: x == y, ("pppw", "sjmn")),
    "dbpl": 5,
    "cczh": Node(lambda x,y: x + y, ("sllz", "lgvd")),
    "zczc": 2,
    "ptdq": Node(lambda x,y: x - y, ("humn", "dvpt")),
    "dvpt": 3,
    "lfqf": 4,
    "humn": humn,
    "ljgn": 2,
    "sjmn": Node(lambda x,y: x * y, ("drzm", "dbpl")),
    "sllz": 4,
    "pppw": Node(lambda x,y: x / y, ("cczh", "lfqf")),
    "lgvd": Node(lambda x,y: x * y, ("ljgn", 'ptdq')),
    "drzm": Node(lambda x,y: x - y, ("hmdt", "zczc")),
    "hmdt": 32
}


def input():
    monkeys = dict()
    number = r"([a-z]+): (\d+)"
    equation = r"([a-z]+): ([a-z]+) ([\*\+\-/]) ([a-z]+)"
    names = []
    with open(path.join(getcwd(), "21_input.txt"), "r") as f:
        for line in f:
            try:
                name, num = re.findall(number, line.strip())[0]
                names += [name]
                monkeys[name] = int(num)
                continue
            except Exception as e:
                pass
            try:
                name, var1, op, var2 = re.findall(equation, line.strip())[0]
                names += [name, var1, var2]
                monkeys[name] = create_lambda(var1, op, var2)
            except Exception as e:
                print(e)
    # no name appears in more than 1 other monkey's entry
    print(list(filter(lambda x: names.count(x) > 2, names)))
    return monkeys


def treeify_input():
    number = r"([a-z]+): (\d+)"
    equation = r"([a-z]+): ([a-z]+) ([\*\+\-/]) ([a-z]+)"
    monkeys = dict()
    def make_eq(op):
        if op == "+":
            return lambda x,y: x + y
        if op == "-":
            return lambda x,y: x - y
        if op == "*":
            return lambda x,y: x * y
        if op == "/":
            return lambda x,y: x / y
    with open(path.join(getcwd(), "21_input.txt"), "r") as f:
        for line in f:
            try:
                name, num = re.findall(number, line.strip())[0]
                monkeys[name] = int(num)
                continue
            except Exception as e:
                pass
            try:
                name, var1, op, var2 = re.findall(equation, line.strip())[0]
                monkeys[name] = Node(make_eq(op), (var1, var2))
            except Exception as e:
                print(e)
    return monkeys


def part_1(monkeys):
    count = len(monkeys.keys())
    answers = dict()
    while len(answers.keys()) < count:
        for k,v in monkeys.items():
            if type(v) == int:
                answers[k] = v
            else:
                try:
                    # print(type(v), v)
                    answers[k] = v(answers)
                except KeyError:
                    pass
    return answers["root"]


def descend(tree, seen=set(), next=""):
    node = tree[next]
    if type(node) == int:
        return node
    if type(node) == sympy.Symbol:
        return node
    x, y = node.args
    return node.func(descend(tree, seen, x), descend(tree, seen, y))



def part_2(monkeys):
    ### lol
    # monkeys["root"] = lambda d: d['vtsj'] == d['tfjf']
    # humn = 0
    # while True:
    #     monkeys["humn"] = humn
    #     if part_1(monkeys): return humn
    #     humn += 1

    ### for real
    # del monkeys["humn"]
    root_branches = monkeys["root"].args
    monkeys["humn"] = sympy.symbols("humn")
    x = descend(monkeys, seen={}, next=root_branches[0])
    y = descend(monkeys, seen={}, next=root_branches[1])
    return sympy.solveset(sympy.Eq(x, y))

if __name__ == "__main__":
    # x = input()
    # print(part_1(x))
    # print(part_1(test_input))
    # print(check_for_multiples())
    t = treeify_input()
    print(part_2(t))
    # print(part_2(test_tree))
