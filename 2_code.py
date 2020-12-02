from collections import Counter
import re


with open("2_data.txt", "r") as f:
    data = f.read().splitlines()

ex = re.compile(r"(?P<llimit>\d+)-(?P<ulimit>\d+) (?P<val>[a-z]): (?P<psswd>\w+)")


def is_valid_one(rule):
    params = ex.match(rule)
    c = Counter(params.group("psswd"))
    return int(params.group("llimit")) <= c[params.group("val")] <= int(params.group("ulimit"))


def is_valid_two(rule):
    params = ex.match(rule)
    a = params.group("psswd")[int(params.group("llimit")) - 1] == params.group("val")
    b = params.group("psswd")[int(params.group("ulimit")) - 1] == params.group("val")
    return a ^ b


total_valid_one = sum(1 for d in data if is_valid_one(d))
print(f"Part One: {total_valid_one}")

total_valid_two = sum(1 for d in data if is_valid_two(d))
print(f"Part Two: {total_valid_two}")
