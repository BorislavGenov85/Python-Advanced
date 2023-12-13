def is_valid_move(rover_row_idx, rover_col_idx, side_row, side_col):
    return 0 <= rover_row_idx + side_row < 6 and 0 <= rover_col_idx + side_col < 6


matrix = [input().split() for _ in range(6)]
commands = input().split(", ")
rover_row = 0
rover_col = 0
deposits = {"W": 0, "M": 0, "C": 0}

directions = {"up": [-1, 0],
              "down": [1, 0],
              "right": [0, 1],
              "left": [0, -1]
              }

for row in range(6):
    for col in range(6):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

for direction in commands:
    next_row, next_col = 0, 0

    if is_valid_move(rover_row, rover_col, directions[direction][0], directions[direction][1]):
        next_row, next_col = rover_row + directions[direction][0], rover_col + directions[direction][1]
    else:
        if direction == "up":
            next_row, next_col = rover_row + 5, rover_col
        elif direction == "down":
            next_row, next_col = rover_row - 5, rover_col
        elif direction == "left":
            next_row, next_col = rover_row, rover_col + 5
        else:
            next_row, next_col = rover_row, rover_col - 5

    if matrix[next_row][next_col] == "W":
        deposit = matrix[next_row][next_col]
        deposits[deposit] += 1
        print(f"Water deposit found at ({next_row}, {next_col})")

    elif matrix[next_row][next_col] == "M":
        deposit = matrix[next_row][next_col]
        deposits[deposit] += 1
        print(f"Metal deposit found at ({next_row}, {next_col})")

    elif matrix[next_row][next_col] == "C":
        deposit = matrix[next_row][next_col]
        deposits[deposit] += 1
        print(f"Concrete deposit found at ({next_row}, {next_col})")

    elif matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    rover_row, rover_col = next_row, next_col

if all(deposits.values()) > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
