import sys
from os import path, getcwd

def part_1():
    elves = [0]
    with open(path.join(getcwd(), "1_input.txt"), "r") as f:
        for line in f:
            try:
                elves[-1] += int(line.rstrip())
            except:
                elves += [0]
    return elves

def part_2(elflist):
    print(sum(sorted(elflist, reverse=True)[:3]))


if __name__ == "__main__":
    part_2(part_1())