import collections
import functools
import inspect
import re
import sys
from itertools import product, permutations
from math import ceil, floor
from operator import itemgetter
from os import path, getcwd


# rocks = [((1,1,1,1),),  # --
#         ((0,1,0), (1,1,1), (0,1,0)),  # +
#         ((0,0,1), (0,0,1), (1,1,1)),  # backwards L
#         ((1,), (1,), (1,), (1,)),  # |
#         ((1,1), (1,1))]  # square


# def part_1():
#     board = []
#     fallen = 0
#     f = open(path.join(getcwd(), "17_input.txt"), "r")
#     rock = None
#     while fallen < 2022:
#         print(fallen)
#         if not rock:
#             rock = rocks[fallen % 5]
#             board = [[0 for _ in range(7)] for _ in range(3 + len(rock))] + board
#             pos = (0, 2)  # (x, y) from L>R T>B for top left corner, 0-indexed
        
#         if not (c := f.read(1)):
#             f.seek(0)
#             c = f.read(1)
#         pos = tuple(a + b for a, b in zip(pos, (1, 0) if c == ">" else (-1, 0)))
#         try:
#             for i, line in enumerate(rock):
#                 x, y = pos
#                 for j, point in enumerate(line):
#                     if board[y + i][x + j] < 2:  # permanent obstacles = 2
#                         board[y + i][x + j] = point
#                     else:
#                         raise IndexError  # placeholder error for running into obstacle
#         except IndexError:
#             board = [[2 if x == 1 else x for x in row] for row in board]
#             rock = None
#             continue
#         else:
#             pos = tuple(a + b for a,b in zip(pos, (0, 1)))
#         try:
#             for i, line in enumerate(rock):
#                 x, y = pos
#                 for j, point in enumerate(line):
#                     if board[y + i][x + j] < 2:  # permanent obstacles = 2
#                         board[y + i][x + j] = point
#                     else:
#                         raise IndexError  # placeholder error for running into obstacle
#         except IndexError:
#             board = [[2 if x == 1 else x for x in row] for row in board]
#             fallen += 1
#             rock = None
#         for row in board:
#             if row == [0] * 7: board.remove(row)
#             else: break
#     return len(board)


rocks = [((0,0), (1,0), (2,0), (3,0)),  # x,y
         ((1,0), (0,1), (1,1), (2,1), (1,2)),
         ((0,0), (1,0), (2,0), (2,1), (2,2)),
         ((0,0), (0,1), (0,2), (0,3)),
         ((0,0), (1,0), (0,1), (1,1))]

f = open(path.join(getcwd(), "17_input.txt"), "r")

def return_move():
    # global f
    if not (c := f.read(1)):
        f.seek(0)
        c = f.read(1)
    return c


def tetris(rounds):
    start_y = 3  # origin is at bottom left
    round = 0
    board = set()

    while round < rounds:
        piece = [(x + 2, y + start_y) for x, y in rocks[round % 5]]
        # blocked = False
        while True:  # not blocked:
            move = 1 if return_move() == ">" else -1
            piece = [(x + move, y) for x,y in piece]
            if any(p in board for p in piece) or any(x < 0 or x > 6 for x, _ in piece):
                move = 0 - move
                piece = [(x + move, y) for x,y in piece]
            piece = [(x, y - 1) for x,y in piece]
            if any(p in board for p in piece) or any(y < 0 for _, y in piece):
                piece = [(x, y + 1) for x,y in piece]
                # blocked = True
                break
        round += 1
        size = len(board)
        board.update(piece)
        start_y = (top := max(y for _, y in board)) + 4
    for y in range(m := max(y for _, y in board), m-100, -1):
        line = ""
        for x in range(7):
            line += "#" if (x, y) in board else "."
        # print(line)
    return start_y - 3


def tetris_loop(rounds):
    start_y = 3  # origin is at bottom left
    round = 0
    board = set()
    file = list(enumerate(open(path.join(getcwd(), "17_input.txt"), "r").read()))
    moves = [x for x in file]
    filling_moves_seen = dict()

    while round < rounds:
        piece = [(x + 2, y + start_y) for x, y in rocks[round % 5]]
        # blocked = False
        while True:  # not blocked:
            try:
                i, c = moves.pop(0)
            except:
                moves = [x for x in file]
                i, c = moves.pop(0)
            move = 1 if c == ">" else -1
            piece = [(x + move, y) for x,y in piece]
            if any(p in board for p in piece) or any(x < 0 or x > 6 for x, _ in piece):
                move = 0 - move
                piece = [(x + move, y) for x,y in piece]
            piece = [(x, y - 1) for x,y in piece]
            if any(p in board for p in piece) or any(y < 0 for _, y in piece):
                piece = [(x, y + 1) for x,y in piece]
                # blocked = True
                break
        rock_i = rocks[round % 5]
        round += 1
        board.update(piece)
        start_y = (top := max(y for _, y in board)) + 4
        if len([x for x, y in board if y == top]) == 7:
            if (k := f"{i} {rock_i}") in filling_moves_seen.keys():
                round_0, score_0 = filling_moves_seen[k]
                print(i, "scores", start_y - 3, score_0, "rounds", round, round_0)
                return start_y - 3 - score_0, round - round_0, round_0
            print(k)
            filling_moves_seen[k] = (round, start_y - 3)
    return start_y - 3

        
def part_1():
    return tetris(2022)


def part_2():
    score_diff, round_diff, round_0 = tetris_loop(1000000000000)
    skipped = floor((r := 1000000000000 - round_0) / round_diff)
    todo = r % round_diff
    exons = tetris(round_0 + todo)
    print(skipped, todo, exons)
    return skipped * score_diff + exons

if __name__ == "__main__":
    # print(return_move(), return_move())
    # print(part_1())
    print(part_2())