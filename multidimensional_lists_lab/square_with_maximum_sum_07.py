rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

total_sum = 0
positions = []
for row in range(rows - 1):
    for col in range(cols - 1):
        result = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if result > total_sum:
            positions = []
            total_sum = result
            positions.append([matrix[row][col], matrix[row][col + 1]])
            positions.append([matrix[row + 1][col], matrix[row + 1][col + 1]])

for item in positions:
    print(*item)
print(total_sum)
