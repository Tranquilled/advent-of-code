import sys
from os import path, getcwd

def part_1():
    score = 0
    with open(path.join(getcwd(), "3_input.txt"), "r") as f:
        for rucksack in f:
            size = int(len(rucksack)/2)
            half_1 = rucksack[0:size]
            half_2 = rucksack [size:]
            for char in half_1:
                if char in half_2:
                    val = ord(char)
                    score += val - 96 if val > 96 else val - 38
                    break # why?
    return score

def part_2():
    score = 0
    with open(path.join(getcwd(), "3_input.txt"), "r") as f:
        count = 0
        common = set()
        for line in f:
            count += 1
            if count == 1:
                common = set(line.rstrip())
            if count == 2:
                common = common.intersection(set(line.rstrip()))
            if count == 3:
                answer = common.intersection(set(line.rstrip())).pop()
                val = ord(answer)
                score += val - 96 if val > 96 else val - 38
                count = 0
    return score

if __name__ == "__main__":
    print(part_2())