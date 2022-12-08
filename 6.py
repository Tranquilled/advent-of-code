import collections
import re
import sys
from os import path, getcwd

def part_1():
    count = 0
    with open(path.join(getcwd(), "6_input.txt"), "r") as f:
        seen = []
        for char in f.read():
            print(seen)
            if len(seen) > 3:
                seen.pop(0)
                if char in seen or len(set(seen)) != len(seen):
                    seen += [char]
                    count += 1
                else:
                    return count + 1
            else:
                seen += [char]
                count += 1


def part_2():
    count = 0
    with open(path.join(getcwd(), "6_input.txt"), "r") as f:
        seen = []
        for char in f.read():
            print(seen)
            if len(seen) > 13:
                seen.pop(0)
                if char in seen or len(set(seen)) != len(seen):
                    seen += [char]
                    count += 1
                else:
                    return count + 1
            else:
                seen += [char]
                count += 1

if __name__ == "__main__":
    print(part_2())