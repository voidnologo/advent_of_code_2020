from collections import defaultdict


with open("5_data.txt", "r") as f:
    data = f.read().splitlines()


def locate_row(row):
    lower = 0
    upper = 127

    for i, c in enumerate(row, 1):
        if c == "B":
            lower += 2 ** (7 - i)
        if c == "F":
            upper -= 2 ** (7 - i)
    return lower


def locate_column(column):
    lower = 0
    upper = 7

    for i, c in enumerate(column, 1):
        if c == "R":
            lower += 2 ** (3 - i)
        if c == "L":
            upper -= 2 ** (3 - i)
    return lower


ids = []
seats = defaultdict(list)
for row in data:
    r = locate_row(row[:7])
    c = locate_column(row[7:])
    seat_id = (r * 8) + c
    ids.append(seat_id)
    seats[r].append(c)


print(max(ids))

for r, c in seats.items():
    if len(c) < 8:
        print(r, c)
