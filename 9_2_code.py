with open("9_data.txt", "r") as f:
    data = f.read().splitlines()


data = [int(_) for _ in data]
TARGET = 15353384


def check_slice(start):
    start = start
    end = start + 1
    success = False

    while end < len(data):
        slice = data[start:end]
        total = sum(slice)
        if total > TARGET:
            break
        if total == TARGET:
            success = True
        end += 1

    return success, end


start = 0
while start < len(data):
    success, end = check_slice(start)
    if success:
        print("<<< WINNER >>>")
        slice = data[start:end]
        low = min(slice)
        high = max(slice)
        total = low + high
        print(f"Min: <{low}>  Max: <{high} Sum: <{total}>")
        break
    start += 1
