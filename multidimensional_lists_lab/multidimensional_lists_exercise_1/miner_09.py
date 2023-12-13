def next_position_is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def next_position(command, row, col, size):
    if command == "up":
        if next_position_is_valid(row - 1, col, size):
            return row - 1, col
    elif command == "right":
        if next_position_is_valid(row, col + 1, size):
            return row, col + 1
    elif command == "down":
        if next_position_is_valid(row + 1, col, size):
            return row + 1, col
    elif command == "left":
        if next_position_is_valid(row, col - 1, size):
            return row, col - 1


size = int(input())
commands = input().split()
matrix = []
miner_row = 0
miner_col = 0
collected_coal = 0
all_coal = 0
flag = True

for row in range(size):
    data = input().split()
    for col in range(len(data)):
        el = data[col]
        if el == "s":
            miner_row = row
            miner_col = col
        elif el == "c":
            all_coal += 1
    matrix.append(data)

for command in commands:
    next_miner_position = next_position(command, miner_row, miner_col, size)
    if not next_miner_position:
        continue

    next_row, next_col = next_miner_position[0], next_miner_position[1]
    if matrix[next_row][next_col] == "e":
        print(f"Game over! ({next_row}, {next_col})")
        flag = False
        break
    elif matrix[next_row][next_col] == "c":
        collected_coal += 1

    matrix[miner_row][miner_col] = "*"
    miner_row = next_row
    miner_col = next_col
    matrix[miner_row][miner_col] = "s"

    if collected_coal == all_coal:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        flag = False
        break

if flag:
    print(f"{all_coal - collected_coal} pieces of coal left. ({miner_row}, {miner_col})")
