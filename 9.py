import collections
import re
import sys
from operator import itemgetter
from os import path, getcwd

dir = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

def between(h, t):
    # surprisingly tricky logic, ensuring that H is always on the same end
    if h > t:
        return range(t + 1, h)
    else:
        return range(t - 1, h, -1)

def part_1():
    H = (0,0)
    T = (0,0)
    visited = {(0,0)}
    with open(path.join(getcwd(), "9_input.txt"), "r") as f:
        count = 0
        for line in f:
            count += 1
            # spent really a lot of time deciding how to do this
            d, n = line.split(" ")
            transform = map(lambda x:int(n)*x, dir[d])
            H = tuple(a + b for a, b in zip(H, transform))
            # if count < 30:
                # print(f"{line.rstrip()}, {H}, {T}")
            if not any(abs(a - b) > 1 for a, b in zip(H, T)):
                # if count < 30:
                #     print("continuing")
                continue
            if not any(a == b for a, b in zip(H, T)):
                if all(a > b for a, b in zip(H, T)):
                    T = tuple(map(lambda x: x + 1, T))
                elif all(a < b for a, b in zip(H, T)):
                    T = tuple(map(lambda x: x - 1, T))
                elif H[0] < T[0] and H[1] > T[1]:
                    T = (T[0] - 1, T[1] + 1)
                else:
                    T = (T[0] + 1, T[1] - 1)
                visited.add(T)
                # if count < 30:
                #     print(f"diagonal {T}")
                # print(f"diagonal, {T}")
            if abs(H[0] - T[0]) > 1:
                # print(f"horiz {[(x, T[1]) for x in between(H[0], T[0])]}")
                v = [(x, T[1]) for x in between(H[0], T[0])]
                T = v[-1]
                visited.update(v)
                # if count < 30:
                #     print(f"horizontal {T}")
            if abs(H[1] - T[1]) > 1:
                v = [(T[0], x) for x in between(H[1], T[1])]
                T = v[-1]
                visited.update(v)
                # if count < 30:
                #     print(f"vertical {T}")
                # print(f"vert {[(T[0], x) for x in between(H[1], T[1])]}")
            if any(abs(a - b) > 1 for a, b in zip(H, T)): # if decoupling
                print(f"{count} {line.rstrip()} {H} {T}")
                print(v)
                break
    return len(visited)
    # return visited
            

def part_2():
    rope = [(0,0)] * 10
    visited = {(0,0)}
    with open(path.join(getcwd(), "9_input.txt"), "r") as f:
        count = 0
        for line in f:
            count += 1
            d, n = line.split(" ")
            transform = map(lambda x:int(n)*x, dir[d])
            rope[0] = tuple(a + b for a, b in zip(rope[0], transform))
            for i in range(9):
                H = rope[i]
                T = rope[i+1]
                # if 1980 < count > 1990:
                #     print(f"{H} {T}")
                if not any(abs(a - b) > 1 for a, b in zip(H, T)):
                    continue
                while not any(a == b for a, b in zip(H, T)):
                    if all(a > b for a, b in zip(H, T)):
                        T = tuple(map(lambda x: x + 1, T))
                    elif all(a < b for a, b in zip(H, T)):
                        T = tuple(map(lambda x: x - 1, T))
                    elif H[0] < T[0] and H[1] > T[1]:
                        T = (T[0] - 1, T[1] + 1)
                    else:
                        T = (T[0] + 1, T[1] - 1)
                    if i == 8:
                        # print("adding")
                        visited.add(T)
                if abs(H[0] - T[0]) > 1:
                    v = [(x, T[1]) for x in between(H[0], T[0])]
                    T = v[-1]
                    if i == 8:
                        # print("horizontal")
                        visited.update(v)
                if abs(H[1] - T[1]) > 1:
                    v = [(T[0], x) for x in between(H[1], T[1])]
                    T = v[-1]
                    if i == 8:
                        # print("vertical")
                        visited.update(v)
                rope[i+1] = T
                if any(abs(a - b) > 1 for a, b in zip(rope[i], rope[i+1])): # if decoupling
                    print(f"{count} {line.rstrip()} {i} {rope[i]} {rope[i+1]}")
                    print(v)
                    return "No"
            if 1980 < count > 1990:
                print(line, rope)
    return len(visited)

def follow(H, T):
    if not any(abs(a - b) > 1 for a, b in zip(H, T)):
        return {}, T
    visited = {T}
    # following logic surprisingly difficult
    while (abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1) and not any(a == b for a, b in zip(H, T)):
        if all(a > b for a, b in zip(H, T)):
            T = tuple(map(lambda x: x + 1, T))
        elif all(a < b for a, b in zip(H, T)):
            T = tuple(map(lambda x: x - 1, T))
        elif H[0] < T[0] and H[1] > T[1]:
            T = (T[0] - 1, T[1] + 1)
        else:
            T = (T[0] + 1, T[1] - 1)
        visited.add(T)
    if abs(H[0] - T[0]) > 1:
        v = [(x, T[1]) for x in between(H[0], T[0])]
        T = v[-1]
        visited.update(v)
    if abs(H[1] - T[1]) > 1:
        v = [(T[0], x) for x in between(H[1], T[1])]
        T = v[-1]
        visited.update(v)
    return visited, T

def part_2_prime():
    rope = [(0,0)] * 10
    visited = {(0,0)}
    with open(path.join(getcwd(), "9_input.txt"), "r") as f:
        count = 0
        for line in f:
            count += 1
            d, n = line.split(" ")
            if 36 < count < 41:
                print(count, rope)
            for i in range(int(n)):
                rope[0] = tuple(a + b for a, b in zip(rope[0], dir[d]))
                for k in range(9):
                    s, p = follow(rope[k], rope[k+1])
                    # if len(s) > 3:
                    #     print(count, line.rstrip(), rope)
                    rope[k+1] = p
                    if k == 8:
                        visited.update(s)
            # if count <30:
            #     print(line, rope)
    return len(visited)


def part_1_prime():
    H = (0,0)
    T = (0,0)
    visited = {(0,0)}
    with open(path.join(getcwd(), "9_input.txt"), "r") as f:
        count = 0
        for line in f:
            count += 1
            # spent really a lot of time deciding how to do this
            d, n = line.split(" ")
            for i in range(int(n)):
                H = tuple(a + b for a, b in zip(H, dir[d]))
                s, T = follow(H, T)
                visited.update(s)
    return len(visited)


if __name__ == "__main__":
    print(part_1())
    print(part_1_prime())
    print(part_2_prime())