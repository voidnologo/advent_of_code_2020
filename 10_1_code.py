from collections import Counter


with open("10_data.txt", "r") as f:
    data = f.read().splitlines()


data = sorted([int(i) for i in data])
wall = [0]
device = [3 + data[-1]]
jolts = wall + data + device

c = Counter()
for idx, i in enumerate(jolts):
    if idx == len(jolts) - 1:
        break
    c.update({jolts[idx + 1] - i: 1})

print(c)
print(f"Val: {c[1] * c[3]}")
