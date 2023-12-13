row, col = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(row):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

for i in range(col):
    total = 0
    for j in range(row):
        num = matrix[j][i]
        total += num
    print(total)
