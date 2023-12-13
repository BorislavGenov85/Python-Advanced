row, col = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    matrix.append(input().split())

while True:
    data = input()
    if data == "END":
        break
    data = data.split()
    command = data[0]
    if command != "swap" or len(data) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in data[1::]]

    if row1 < 0 or row1 > row - 1 or row2 < 0 or row2 > row - 1 or \
            col1 < 0 or col1 > col - 1 or col2 < 0 or col2 > col - 1:
        print("Invalid input!")
        continue
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for part in matrix:
            print(*part)
