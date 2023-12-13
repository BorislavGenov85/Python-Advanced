matrix = [input().split() for _ in range(6)]
coord = input()
pos = []
directions = {"up": [-1, 0],
              "down": [1, 0],
              "right": [0, 1],
              "left": [0, -1]
              }

for ch in coord:
    if ch.isdigit():
        pos.append(ch)

row, col = int(pos[0]), int(pos[1])
while True:
    data = input()

    if data == "Stop":
        break

    data = data.split(", ")
    command = data[0]
    direction = data[1]

    if command == "Create":
        value = data[2]
        row, col = row + directions[direction][0], col + directions[direction][1]
        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif command == "Update":
        value = data[2]
        row, col = row + directions[direction][0], col + directions[direction][1]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    elif command == "Delete":
        row, col = row + directions[direction][0], col + directions[direction][1]
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    else:
        row, col = row + directions[direction][0], col + directions[direction][1]
        if matrix[row][col] != ".":
            print(matrix[row][col])

[print(" ".join(x)) for x in matrix]
