with open("8_data.txt", "r") as f:
    data = f.read().splitlines()


class InfiniteLoop(Exception):
    pass


def run_instructions(mod_index):
    ip = 0  # instruction pointer
    accumulator = 0
    seen = set()
    while True:
        command, val = data[ip].split()
        if ip == mod_index:
            if command == "nop":
                command = "jmp"
            elif command == "jmp":
                command = "nop"
        if command == "nop":
            offset = 1
        if command == "acc":
            offset = 1
            accumulator += int(val)
        if command == "jmp":
            offset = int(val)

        next_ip = ip + offset
        if next_ip in seen:
            raise InfiniteLoop()
        seen.add(next_ip)
        ip = next_ip
        print(ip, len(data))
        if ip >= len(data):
            break

    return accumulator


instruction_counter = 0
while True:
    if instruction_counter > len(data):
        raise Exception("Looped too many times with no solution")
    try:
        print("Successful run:", run_instructions(instruction_counter))
        break
    except InfiniteLoop:
        instruction_counter += 1
