import collections
import re
import sys
from os import path, getcwd

def parse():
    rows = []
    crates = collections.defaultdict(list)
    with open(path.join(getcwd(), "5_input_1.txt"), "r") as f:
        for line in f:
            rows += [re.split("[\[\]]", line.rstrip())]

    column = 0
    for row in rows:
        for i in row:
            if "         " == i:
                crates[column] += [" ", " "]
            elif i in ("    ", "     "):
                crates[column] += " "
            elif i in (" ", ""):
                continue
            else:
                crates[column] += i
        column += 1
    column_crates = collections.defaultdict(str)
    for i in range(max([len(crates[row]) for row in crates])):
        for j in crates:
            try:
                column_crates[i] += crates[j][i]
            except:
                column_crates[i] += " "
    return([column_crates[x].strip() for x in column_crates])

def part_1(crates):
    with open(path.join(getcwd(), "5_input.txt"), "r") as f:
        for line in f:
            n = re.match(r"move (\d+) from (\d) to (\d)", line)
            amount = int(n.group(1))
            frm = int(n.group(2)) - 1
            to = int(n.group(3)) - 1
            # print(f"before {crates[to]} {crates[frm][0:amount][::-1]} {crates[frm]}")
            crates[to] = crates[frm][0:amount][::-1] + crates[to]
            crates[frm] = crates[frm][amount:]
            # print(f"after {amount} {frm} {to}")
            # print(crates[to])
            # print(crates[frm])
    return crates

def part_2(crates):
    with open(path.join(getcwd(), "5_input.txt"), "r") as f:
        for line in f:
            n = re.match(r"move (\d+) from (\d) to (\d)", line)
            amount = int(n.group(1))
            frm = int(n.group(2)) - 1
            to = int(n.group(3)) - 1
            # print(f"before {crates[to]} {crates[frm][0:amount][::-1]} {crates[frm]}")
            crates[to] = crates[frm][0:amount] + crates[to]
            crates[frm] = crates[frm][amount:]
            # print(f"after {amount} {frm} {to}")
            # print(crates[to])
            # print(crates[frm])
    return crates


if __name__ == "__main__":
    print(part_2(parse()))