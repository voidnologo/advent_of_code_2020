from itertools import combinations


class NotFound(Exception):
    pass


with open("9_data.txt", "r") as f:
    data = f.read().splitlines()


data = [int(_) for _ in data]
start = 0
end = 25

while end < len(data):
    slice = data[start:end]
    compare = data[end]
    totals = set(sum(x) for x in combinations(slice, 2))
    if compare in totals:
        start += 1
        end += 1
    else:
        raise NotFound(f"{compare} not in window")
