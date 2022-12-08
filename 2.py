import sys
from os import path, getcwd

def part_1():
    with open(path.join(getcwd(), "2_input.txt"), "r") as f:
        points = {
            "A X": 1+3,
            "A Y": 2+6,
            "A Z": 3+0,
            "B X": 1+0,
            "B Y": 2+3,
            "B Z": 3+6,
            "C X": 1+6,
            "C Y": 2+0,
            "C Z": 3+3,
        }
        score = 0
        for line in f:
            score += points[line.rstrip()]
    return score

def part_2():
    points = {
        "A X": 0+3, # rock lose
        "A Y": 3+1, # rock tie
        "A Z": 6+2, # rock win
        "B X": 0+1, # paper lose
        "B Y": 3+2, # paper tie
        "B Z": 6+3, # paper win
        "C X": 0+2, # scissors lose
        "C Y": 3+3, # scissors tie
        "C Z": 6+1, # scissors win
    }
    with open(path.join(getcwd(), "2_input.txt"), "r") as f:
        score = 0
        for line in f:
            score += points[line.rstrip()]
    return score


if __name__ == "__main__":
    print(part_2())