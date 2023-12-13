from collections import deque


def white_move(row, col, oponent):

    if row - 1 == oponent[0] and col - 1 == oponent[1]:
        print(f"Game over! White win, capture on {positions_col[col - 1]}{position_row[row - 1]}.")
        raise SystemExit

    if row - 1 == oponent[0] and col + 1 == oponent[1]:
        print(f"Game over! White win, capture on {positions_col[col + 1]}{position_row[row - 1]}.")
        raise SystemExit

    return row - 1, col


def black_move(row, col, oponent):

    if row + 1 == oponent[0] and col + 1 == oponent[1]:
        print(f"Game over! Black win, capture on {positions_col[col + 1]}{position_row[row + 1]}.")
        raise SystemExit

    if row + 1 == oponent[0] and col - 1 == oponent[1]:
        print(f"Game over! Black win, capture on {positions_col[col - 1]}{position_row[row + 1]}.")
        raise SystemExit

    return row + 1, col


def start():

    w_row_col = []
    b_row_col = []

    for row in range(len(matrix)):
        el = matrix[row]
        for col in range(len(el)):
            if el[col] == "w":
                w_row_col.extend([row, col])
            elif el[col] == "b":
                b_row_col.extend([row, col])
    players.append(w_row_col)
    players.append(b_row_col)

    while True:

        w_next_row, w_next_col = white_move(w_row_col[0], w_row_col[1], b_row_col)
        w_row_col[0], w_row_col[1] = w_next_row, w_next_col
        if w_next_row == 0:
            print(
                f"Game over! White pawn is promoted to a queen at {positions_col[w_next_col]}{position_row[w_next_row]}.")
            raise SystemExit

        b_next_row, b_next_col = black_move(b_row_col[0], b_row_col[1], w_row_col)
        b_row_col[0], b_row_col[1] = b_next_row, b_next_col
        if b_next_row == 7:
            print(
                f"Game over! Black pawn is promoted to a queen at {positions_col[b_next_col]}{position_row[b_next_row]}.")
            raise SystemExit


matrix = [input().split() for _ in range(8)]
players = deque()
position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}
start()


# second solution
# from collections import deque
#
#
# def white_move(row, col, oponent):
#
#     if row - 1 == oponent[0] and col - 1 == oponent[1]:
#         print(f"Game over! White win, capture on {positions_col[col - 1]}{position_row[row - 1]}.")
#         raise SystemExit
#
#     if row - 1 == oponent[0] and col + 1 == oponent[1]:
#         print(f"Game over! White win, capture on {positions_col[col + 1]}{position_row[row - 1]}.")
#         raise SystemExit
#
#     return row - 1, col
#
#
# def black_move(row, col, oponent):
#
#     if row + 1 == oponent[0] and col + 1 == oponent[1]:
#         print(f"Game over! Black win, capture on {positions_col[col + 1]}{position_row[row + 1]}.")
#         raise SystemExit
#
#     if row + 1 == oponent[0] and col - 1 == oponent[1]:
#         print(f"Game over! Black win, capture on {positions_col[col - 1]}{position_row[row + 1]}.")
#         raise SystemExit
#
#     return row + 1, col
#
#
# matrix = [input().split() for _ in range(8)]
# players = deque()
# position_row = {
#     0: "8",
#     1: "7",
#     2: "6",
#     3: "5",
#     4: "4",
#     5: "3",
#     6: "2",
#     7: "1",
# }
# positions_col = {
#     0: "a",
#     1: "b",
#     2: "c",
#     3: "d",
#     4: "e",
#     5: "f",
#     6: "g",
#     7: "h",
# }
# w_row_col = []
# b_row_col = []
#
# for row in range(len(matrix)):
#     el = matrix[row]
#     for col in range(len(el)):
#         if el[col] == "w":
#             w_row_col.extend([row, col])
#         elif el[col] == "b":
#             b_row_col.extend([row, col])
# players.append(w_row_col)
# players.append(b_row_col)
#
# while True:
#     w_next_row, w_next_col = white_move(w_row_col[0], w_row_col[1], b_row_col)
#     w_row_col[0], w_row_col[1] = w_next_row, w_next_col
#     if w_next_row == 0:
#         print(
#             f"Game over! White pawn is promoted to a queen at {positions_col[w_next_col]}{position_row[w_next_row]}.")
#         break
#
#     b_next_row, b_next_col = black_move(b_row_col[0], b_row_col[1], w_row_col)
#     b_row_col[0], b_row_col[1] = b_next_row, b_next_col
#     if b_next_row == 7:
#         print(
#             f"Game over! Black pawn is promoted to a queen at {positions_col[b_next_col]}{position_row[b_next_row]}.")
#         break
