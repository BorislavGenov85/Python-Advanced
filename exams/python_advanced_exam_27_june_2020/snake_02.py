def move(idx, idx2, territory, lairs_pos, eaten_food):

    if territory[idx][idx2] == "*":
        eaten_food += 1
        territory[idx][idx2] = "S"
        return idx, idx2, territory, lairs_pos, eaten_food

    elif territory[idx][idx2] == "B":
        territory[idx][idx2] = "."
        lairs_pos.remove([idx, idx2])
        idx, idx2 = lairs_pos[0][0], lairs_pos[0][1]
        territory[idx][idx2] = "S"
        lairs_pos.clear()
        return idx, idx2, territory, lairs_pos, eaten_food

    else:
        territory[idx][idx2] = "S"
        return idx, idx2, territory, lairs_pos, eaten_food


def is_valid_move(idx1, idx2, border):
    return 0 <= idx1 < border and 0 <= idx2 < border


size = int(input())
territory = []
snake_row, snake_col = 0, 0
lairs_pos = []
eaten_food = 0
out = False
fed = False

for row in range(size):
    line = list(input())
    territory.append(line)
    for col in range(len(line)):
        el = line[col]

        if el == "S":
            snake_row, snake_col = row, col
        if el == "B":
            lairs_pos.append([row, col])

while True:
    command = input()
    territory[snake_row][snake_col] = "."

    if command == "up":
        if not is_valid_move(snake_row - 1, snake_col, size):
            out = True
            break
        else:
            snake_row, snake_col, territory, lairs_pos, eaten_food =\
                move(snake_row - 1, snake_col, territory, lairs_pos, eaten_food)

    elif command == "down":
        if not is_valid_move(snake_row + 1, snake_col, size):
            out = True
            break
        else:
            snake_row, snake_col, territory, lairs_pos, eaten_food = \
                move(snake_row + 1, snake_col, territory, lairs_pos, eaten_food)

    elif command == "left":
        if not is_valid_move(snake_row, snake_col - 1, size):
            out = True
            break
        else:
            snake_row, snake_col, territory, lairs_pos, eaten_food = \
                move(snake_row, snake_col - 1, territory, lairs_pos, eaten_food)

    elif command == "right":
        if not is_valid_move(snake_row, snake_col + 1, size):
            out = True
            break
        else:
            snake_row, snake_col, territory, lairs_pos, eaten_food = \
                move(snake_row, snake_col + 1, territory, lairs_pos, eaten_food)

    if eaten_food == 10:
        fed = True
        break

if out:
    print("Game over!")

if fed:
    print("You won! You fed the snake.")
print(f"Food eaten: {eaten_food}")
[print(''.join(row))for row in territory]
