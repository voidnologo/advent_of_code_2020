with open("8_data.txt", "r") as f:
    data = f.read().splitlines()


ip = 0  # instruction pointer
accumulator = 0
seen = set()


while True:
    command, val = data[ip].split()
    if command == "nop":
        offset = 1
    if command == "acc":
        offset = 1
        accumulator += int(val)
    if command == "jmp":
        offset = int(val)

    next_ip = ip + offset
    if next_ip in seen:
        break
    seen.add(next_ip)
    ip = next_ip


print("Acc:", accumulator)
