def move(c_row, c_col, pl_n_r, pl_n_c, iterable, text, number):
    if is_legal_move(pl_n_r, pl_n_c, number):
        iterable[c_row][c_col] = "-"
        if iterable[pl_n_r][pl_n_c] != "-":
            text.append(iterable[pl_n_r][pl_n_c])
        iterable[pl_n_r][pl_n_c] = "P"
        c_row, c_col = next_row, next_col
        return c_row, c_col, iterable, text
    else:
        if text:
            text.pop()
        return c_row, c_col, iterable, text


def is_legal_move(idx1, idx2, num):
    return 0 <= idx1 < num and 0 <= idx2 < num


word = list(input())
size = int(input())
player_row, player_col = 0, 0
field = []

for row in range(size):
    current_row = list(input())
    field.append(current_row)
    for col in range(len(current_row)):
        ch = current_row[col]
        if ch == "P":
            player_row = row
            player_col = col

number = int(input())
for _ in range(number):
    command = input()

    if command == "up":
        next_row, next_col = player_row - 1, player_col
        player_row, player_col, field, word = move(player_row, player_col, next_row, next_col, field, word, size)

    elif command == "down":
        next_row, next_col = player_row + 1, player_col
        player_row, player_col, field, word = move(player_row, player_col, next_row, next_col, field, word, size)

    elif command == "left":
        next_row, next_col = player_row, player_col - 1
        player_row, player_col, field, word = move(player_row, player_col, next_row, next_col, field, word, size)

    elif command == "right":
        next_row, next_col = player_row, player_col + 1
        player_row, player_col, field, word = move(player_row, player_col, next_row, next_col, field, word, size)

print(''.join(word))
[print(''.join(row)) for row in field]
