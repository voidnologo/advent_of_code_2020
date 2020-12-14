from collections import Counter
from itertools import chain


with open("11_data.txt", "r") as f:
    GRID = f.read().splitlines()

ROW_COUNT = len(GRID)
COL_COUNT = len(GRID[0])


EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."
ADJACENT_GRID = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def get_surrounding(y, x):
    surrounding = []
    for delta_y, delta_x in ADJACENT_GRID:
        ypos = y + delta_y
        xpos = x + delta_x
        if (ROW_COUNT <= ypos) or (ypos < 0) or (COL_COUNT <= xpos) or (xpos < 0):
            surrounding.append(None)
        else:
            value = GRID[ypos][xpos]
            surrounding.append(value)
    return surrounding


def get_next_value(value, surrounding):
    counts = Counter(surrounding)
    if value == EMPTY and counts[OCCUPIED] == 0:
        return OCCUPIED
    if value == OCCUPIED and counts[OCCUPIED] >= 4:
        return EMPTY
    return value


while True:
    next_grid = []
    for y, row in enumerate(GRID):
        next_row = ""
        for x, seat in enumerate(row):
            val = GRID[y][x]
            surrounding = get_surrounding(y, x)
            next_val = get_next_value(val, surrounding)
            next_row += next_val
        next_grid.append(next_row)

    if next_grid == GRID:
        break
    GRID = next_grid


import jpprint

jpprint.jpprint(GRID)
c = Counter(chain(*GRID))
print(c)
