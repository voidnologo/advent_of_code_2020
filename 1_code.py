from itertools import combinations
from math import prod


with open("1_data.txt", "r") as f:
    data = f.read().splitlines()


print(next((c, prod(c)) for c in combinations(data, 3) if sum(c) == 2020))
