n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

needed_symbol = input()

position = []
flag = False
for row in range(n):
    for col in range(n):
        symbol = matrix[row][col]
        if needed_symbol == matrix[row][col]:
            position.append(f"({row}, {col})")
            flag = True
            break
    if flag:
        break

if position:
    print(*position)
else:
    print(f"{needed_symbol} does not occur in the matrix")
