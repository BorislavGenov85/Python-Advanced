matrix_row_col = int(input())

matrix = []

for _ in range(matrix_row_col):
    data = [int(x) for x in input().split()]
    matrix.append(data)

while True:
    data = input()
    if data == "END":
        break
    data = data. split()
    command = data[0]
    row, col, value = [int(x) for x in data[1:]]

    if row < 0 or col < 0 or row >= matrix_row_col or col >= matrix_row_col:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")

# second solution


# def is_valid_coordinates(row, col):
#     if 0 <= row < size and 0 <= col < size:
#         return True
#     return False
#
#
# size = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(size)]
#
# while True:
#     data = input().split()
#
#     if data[0] == "END":
#         break
#
#     command = data[0]
#     row = int(data[1])
#     col = int(data[2])
#     value = int(data[3])
#
#     if command == "Add":
#         if is_valid_coordinates(row, col):
#             matrix[row][col] += value
#
#         else:
#             print("Invalid coordinates")
#
#     else:
#         if is_valid_coordinates(row, col):
#             matrix[row][col] -= value

#         else:
#             print("Invalid coordinates")
#
# [print(*row) for row in matrix]
