def is_valid_move(idx1, idx2, num):
    return 0 <= idx1 < num and 0 <= idx2 < num


def move_up(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_up(q_row - 1, q_col, iterable, border)
    else:
        return False


def move_down(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_down(q_row + 1, q_col, iterable, border)
    else:
        return False


def move_right(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_right(q_row, q_col + 1, iterable, border)
    else:
        return False


def move_left(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_left(q_row, q_col - 1, iterable, border)
    else:
        return False


def move_right_up(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_right_up(q_row - 1, q_col + 1, iterable, border)
    else:
        return False


def move_left_up(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_left_up(q_row - 1, q_col - 1, iterable, border)
    else:
        return False


def move_right_down(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_right_down(q_row + 1, q_col + 1, iterable, border)
    else:
        return False


def move_left_down(q_row, q_col, iterable, border):
    if is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == "K":
        return True
    elif is_valid_move(q_row, q_col, border) and iterable[q_row][q_col] == ".":
        return move_left_down(q_row + 1, q_col - 1, iterable, border)
    else:
        return False


size = 8
board = []
king_row, king_col = 0, 0
queens_pos = []

for row in range(size):
    current_row = input().split()
    board.append(current_row)
    for col in range(len(current_row)):
        ch = current_row[col]
        if ch == "K":
            king_row, king_col = row, col
        elif ch == "Q":
            queens_pos.append([row, col])

capturing_king = []
for item in queens_pos:
    queens_cur_row = item[0]
    queens_cur_col = item[1]

    if move_up(queens_cur_row - 1, queens_cur_col, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_down(queens_cur_row + 1, queens_cur_col, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_left(queens_cur_row, queens_cur_col - 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_right(queens_cur_row, queens_cur_col + 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_right_up(queens_cur_row - 1, queens_cur_col + 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_left_up(queens_cur_row - 1, queens_cur_col - 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_right_down(queens_cur_row + 1, queens_cur_col + 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue
    if move_left_down(queens_cur_row + 1, queens_cur_col - 1, board, size):
        capturing_king.append([queens_cur_row, queens_cur_col])
        continue

if capturing_king:
    [print(el)for el in capturing_king]
else:
    print("The king is safe!")
