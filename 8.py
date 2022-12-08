import collections
import re
import sys
from os import path, getcwd


def array_trees():
    with open(path.join(getcwd(), "8_input.txt"), "r") as f:
        trees = []
        for line in f:
            trees += [[int(x) for x in line.rstrip()]]
    return trees

def is_visible(trees, i, j):
    h = trees[i][j]
    s = len(trees)
    if 0 in (i, j) or s - 1 in (i,j): return True  # trees is square
    # print([x for x in [trees[y][j] for y in range(0, i)]])
    if all(h > x for x in [trees[y][j] for y in range(0, i)]): return True
    if all(h > x for x in [trees[y][j] for y in range(i+1, s)]): return True
    if all(h > x for x in [trees[i][y] for y in range(0, j)]): return True
    if all(h > x for x in [trees[i][y] for y in range(j+1, s)]): return True
    return False

def look(line, h):
    d = 0
    # print(h, line)
    for i in line:
        # if i < h:
        #     d += 1
        # else:
        #     break
        d += 1  # the blocking tree is visible
        if i >= h:
            break
    return d

def score(trees, i, j):
    h = trees[i][j]
    size = len(trees)
    if 0 in (i, j) or size - 1 in (i,j): return 0
    if h == 0: return 1
    # print(i,j,h)
    # print([trees[y][j] for y in range(0, i)])
    w = look([trees[y][j] for y in range(0, i)][::-1], h)  # count down for up and left
    # print([trees[y][j] for y in range(i+1, s)])
    s = look([trees[y][j] for y in range(i+1, size)], h)
    a = look([trees[i][y] for y in range(0, j)][::-1], h)
    d = look([trees[i][y] for y in range(j+1, size)], h)
    if i < 3 and j < 3:
        print(h, i, j, w, a, s, d)
    return w * a * s * d

def part_1(trees):
    visible = 0
    for i in range(len(trees)):
        for j in range(len(trees)):
            if is_visible(trees, i, j): visible += 1
    return visible

def part_2(trees):
    scores = set()
    # for i in range(3):
    #     for j in range(3):
    for i in range(len(trees)):
        for j in range(len(trees)):
            scores.add(score(trees, i, j))
    return max(scores)

if __name__ == "__main__":
    print(part_2(array_trees()))
    # print(array_trees())