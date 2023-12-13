def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def next_position(row, col, command):
    if command == "U":
        return row - 1, col
    elif command == "R":
        return row, col + 1
    elif command == "D":
        return row + 1, col
    elif command == "L":
        return row, col - 1


rows, cols = [int(x) for x in input().split()]

matrix = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    data = list(input())
    matrix.append(data)
    for col in range(len(data)):
        el = data[col]
        if el == "P":
            player_row = row
            player_col = col
        elif el == "B":
            bunnies.add(f"{row} {col}")

directions = input()

won = False
dead = False

matrix[player_row][player_col] = "."

for command in directions:
    next_row, next_col = next_position(player_row, player_col, command)

    if is_outside(next_row, next_col, rows, cols):
        won = True

    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunni in bunnies:
        bunni_row, bunni_col = [int(x) for x in bunni.split()]

        if not is_outside(bunni_row - 1, bunni_col, rows, cols):
            new_bunnies.add(f"{bunni_row - 1} {bunni_col}")
            matrix[bunni_row - 1][bunni_col] = "B"
        if not is_outside(bunni_row, bunni_col + 1, rows, cols):
            new_bunnies.add(f"{bunni_row} {bunni_col + 1}")
            matrix[bunni_row][bunni_col + 1] = "B"
        if not is_outside(bunni_row, bunni_col - 1, rows, cols):
            new_bunnies.add(f"{bunni_row} {bunni_col - 1}")
            matrix[bunni_row][bunni_col - 1] = "B"
        if not is_outside(bunni_row + 1, bunni_col, rows, cols):
            new_bunnies.add(f"{bunni_row + 1} {bunni_col}")
            matrix[bunni_row + 1][bunni_col] = "B"

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == "B":
        dead = True

    if won or dead:
        break

for row in matrix:
    print(*row, sep="")

if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")

