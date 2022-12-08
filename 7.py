import collections
import re
import sys
from os import path, getcwd


def part_1():
    tree = make_tree()
    # return traverse_and_sum(tree, 0)
    # return [k for k, v in sorted(iter(traverse_and_sum(tree, dict(), []).items()), key=lambda i: i[1])]
    return sum([v for v in iter(traverse_and_sum(tree["/"], dict(), ["/"]).values()) if v <= 100000])

# def traverse_and_sum(tree, size): # sanity check with total size of /
#     for k,v in iter(tree.items()):
#         if type(v) == int:
#             size += v
#         else:
#             size = traverse_and_sum(v, size)
#     return size

def part_2():
    tree = make_tree()
    sizes = traverse_and_sum(tree, dict(), [])
    needed = 30000000 - (70000000 - sizes["_/"])
    return [v for k, v in sorted(iter(sizes.items()), key=lambda i: i[1]) if v > needed]
    


def traverse_and_sum(tree, sizes, parents):
    # if len(parents) < 5:
    #     print(parents)
    for k,v in iter(tree.items()):
        cwd = f"{('_').join(parents)}_{k}" # why does this make / into _/ ?
        if type(v) == int:
            for dir in parents:
                # sizes[dir] += v  # this goddamn line
                try:
                    sizes[dir] += v
                except KeyError:
                    sizes[dir] = v
        else:
            sizes = traverse_and_sum(v, sizes, [cwd] + parents)
    return sizes


def make_tree():
    tree = {"/": dict()}
    cwd = ["/"]
    with open(path.join(getcwd(), "7_input.txt"), "r") as f:
        for line in f:
            line = line.rstrip()
            # try:
            if "$ cd" in line:
                dir = line.split(" ")[2]
                if dir == "/":
                    cwd = ["/"]
                elif dir == "..":
                    cwd.pop()
                else:
                    cwd += [dir]
            elif "dir " in line:
                n = line.split(" ")[1]
                traverse_and_add(tree, cwd, n, "dir")
            elif line == "$ ls":
                pass
            else:
                n = re.match("(\d+) (.+)", line)
                size = n.group(1)
                file = n.group(2)
                traverse_and_add(tree, cwd, (file, int(size)), "file")
            # except Exception as e:
            #     print(line, e)
    return tree

def traverse_and_add(tree, list, new, new_type):
    x = tree
    for i in list:
        x = x[i]
    if new_type == "dir":
        x[new] = dict()
    if new_type == "file":
        x[new[0]] = new[1]

if __name__ == "__main__":
    print(part_2())