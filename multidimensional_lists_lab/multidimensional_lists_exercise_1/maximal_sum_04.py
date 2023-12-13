rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
best_row = 0
best_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row = row
            best_col = col

print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")

# second solution

# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(el) for el in input().split()] for _ in range(rows)]
#
# max_sum = float("-inf")
# sub_matrix = []
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         first = matrix[row][col:col + 3]
#         second = matrix[row + 1][col:col + 3]
#         third = matrix[row + 2][col:col + 3]
#
#         result = sum(first) + sum(second) + sum(third)
#
#         if result > max_sum:
#             max_sum = result
#             sub_matrix = [first, second, third]
#
# print(f"Sum = {max_sum}")
# [print(*row)for row in sub_matrix]