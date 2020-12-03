from math import prod


with open("3_data.txt", "r") as f:
    data = f.read().splitlines()


def char_at(line, pos):
    index = pos % len(line)
    return line[index]


# == Part 1 ==========

tree_count = 0
pos = 0
for line in data:
    if char_at(line, pos) == "#":
        tree_count += 1
    pos += 3


print(f"{tree_count =}")

# == END Part 1 ==========


# == Part 2 ==========


def pos_tracker(x, y):
    x_loc = 0
    y_loc = 0
    while True:
        yield x_loc, y_loc
        x_loc += x
        y_loc += y


slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

totals = []
for slope in slopes:
    locator = pos_tracker(*slope)
    pos, line_number = next(locator)
    tree_count = 0
    while line_number < len(data):
        if char_at(data[line_number], pos) == "#":
            tree_count += 1
        pos, line_number = next(locator)
    totals.append(tree_count)

print(f"{totals =}")
print(prod(totals))
