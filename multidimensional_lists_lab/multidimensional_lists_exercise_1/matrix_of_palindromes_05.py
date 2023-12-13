row, col = [int(x) for x in input().split()]

matrix = []

for i in range(row):
    result = []
    for j in range(col):
        result.append(f"{chr(97 + i)}{chr(97 + j + i)}{chr(97 + i)}")
    matrix.append(result)

for part in matrix:
    print(" ".join(part))

# second solution

# rows, cols = [int(x) for x in input().split()]
#
# start = ord("a")
# matrix = []
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")
#     print()
