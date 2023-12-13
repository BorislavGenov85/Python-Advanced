def is_valid_direction(idx, idx2, border):
    return 0 <= idx < border and 0 <= idx2 < border


size = int(input())
bombs = int(input())
bombs_pos = []
board = [[0 for _ in range(size)] for _ in range(size)]

for _ in range(bombs):
    current_bomb_pos = input()
    bombs_pos.append(current_bomb_pos)

for el in bombs_pos:
    el_row, el_col = el.strip("(").strip(")").split(", ")
    el_row = int(el_row)
    el_col = int(el_col)

    board[el_row][el_col] = "*"

for i in range(len(board)):
    elements = board[i]
    for j in range(len(elements)):
        current_el = board[i][j]
        if current_el == "*":
            continue
        else:
            if is_valid_direction(i - 1, j, size) and board[i - 1][j] == "*":
                board[i][j] += 1
            if is_valid_direction(i + 1, j, size) and board[i + 1][j] == "*":
                board[i][j] += 1
            if is_valid_direction(i, j - 1, size) and board[i][j - 1] == "*":
                board[i][j] += 1
            if is_valid_direction(i, j + 1, size) and board[i][j + 1] == "*":
                board[i][j] += 1
            if is_valid_direction(i - 1, j - 1, size) and board[i - 1][j - 1] == "*":
                board[i][j] += 1
            if is_valid_direction(i - 1, j + 1, size) and board[i - 1][j + 1] == "*":
                board[i][j] += 1
            if is_valid_direction(i + 1, j + 1, size) and board[i + 1][j + 1] == "*":
                board[i][j] += 1
            if is_valid_direction(i + 1, j - 1, size) and board[i + 1][j - 1] == "*":
                board[i][j] += 1

[print(' '.join([str(x) for x in row]))for row in board]
