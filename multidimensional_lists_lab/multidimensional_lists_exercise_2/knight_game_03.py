def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def is_knight(row, col, matrix):
    return matrix[row][col] == "K"


def get_attack_counter(row, col, matrix):
    result = 0
    if is_inside(row - 2, col - 1, len(matrix)) and is_knight(row - 2, col - 1, matrix):
        result += 1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result += 1
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result += 1
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result += 1
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result += 1
    return result


size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    table = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter

    if len(table) == 0:
        break

    knight_row, knight_col = 0, 0
    best_counter = 0
    for coords, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]

    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)


# second solution

# size = int(input())
# matrix = [list(input()) for _ in range(size)]
#
# directions = [
#     [-2, -1],  # up 2 left 1
#     [-2, 1],  # up 2 right 1
#     [-1, -2],  # up 1 left 2
#     [-1, 2],  # up 1 right 2
#     [1, -2],  # down 1 left 2
#     [1, 2],  # down 1 right 2
#     [2, -1],  # down 2 left 1
#     [2, 1]  # down 2 right 1
# ]
# knight_position = []
# removed_knights = 0
#
# while True:
#     max_attacks = 0
#     knight_with_most_attack_position = []
#
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == "K":
#                 attacks = 0
#
#                 for pos in directions:
#                     pos_row = row + pos[0]
#                     pos_col = col + pos[1]
#
#                     if 0 <= pos_row < size and 0 <= pos_col < size:
#                         if matrix[pos_row][pos_col] == "K":
#                             attacks += 1
#
#                 if attacks > max_attacks:
#                     knight_with_most_attack_position = [row, col]
#                     max_attacks = attacks
#
#     if knight_with_most_attack_position:
#         matrix[knight_with_most_attack_position[0]][knight_with_most_attack_position[1]] = "0"
#         removed_knights += 1
#     else:
#         break
#
# print(removed_knights)
