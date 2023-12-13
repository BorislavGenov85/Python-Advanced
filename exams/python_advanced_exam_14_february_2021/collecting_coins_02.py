from math import floor


def is_inside(idx1, idx2, field_limit):
    return 0 <= idx1 < field_limit and 0 <= idx2 < field_limit


def player_move(player_row_idx, player_col_idx, command, number):
    if command == "up":
        if is_inside(player_row_idx - 1, player_col_idx, number):
            return player_row_idx - 1, player_col_idx
        else:
            return number - 1, player_col_idx

    elif command == "down":
        if is_inside(player_row_idx + 1, player_col_idx, number):
            return player_row_idx + 1, player_col_idx
        else:
            return 0, player_col_idx

    elif command == "left":
        if is_inside(player_row_idx, player_col_idx - 1, number):
            return player_row_idx, player_col_idx - 1
        else:
            return player_row_idx, size - 1

    elif command == "right":
        if is_inside(player_row_idx, player_col_idx + 1, number):
            return player_row_idx, player_col_idx + 1
        else:
            return player_row_idx, 0


size = int(input())
field = []
player_row = 0
player_col = 0

collected_coins = 0
coins_to_win = 100
path = []

for row in range(size):
    field_row = input().split()
    field_row = [int(x) if x.isdigit() else x for x in field_row]
    field.append(field_row)
    for col in range(len(field_row)):
        el = field_row[col]
        if el == "P":
            player_row = row
            player_col = col

path.append([player_row, player_col])
field[player_row][player_col] = 0
win = False

while True:
    direction = input()

    next_row, next_col = player_move(player_row, player_col, direction, size)
    if field[next_row][next_col] != "X":
        collected_coins += field[next_row][next_col]
        path.append([next_row, next_col])
        field[next_row][next_col] = 0
        player_row, player_col = next_row, next_col

    else:
        if collected_coins != 0:
            collected_coins = floor(collected_coins / 2)
            path.append([next_row, next_col])
            break
        else:
            collected_coins = 0
            path.append([next_row, next_col])
            break

    if collected_coins >= coins_to_win:
        win = True
        break

if win:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path:")
[print(x) for x in path]
