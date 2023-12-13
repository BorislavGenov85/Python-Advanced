n = int(input())
matrix = []

for _ in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

total = 0
for row in range(n):
    for col in range(n):
        num = matrix[row][col]
        if row == col:
            total += num

print(total)
