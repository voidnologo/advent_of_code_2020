import re


with open("6_data.txt", "r") as f:
    data = f.read().splitlines()


responses = []
e = ""
for line in data:
    if line != "":
        e += line
    else:
        responses.append(e)
        e = ""


# == Part 1 ==========

total = sum(len(s) for s in (set(r.replace(" ", "")) for r in responses))

print(f"Part One:", total)


# == Part 2 ==========

total = sum(len(set(r.split()[0]).intersection(*r.split())) for r in responses)

print(f"Part Two:", total)
