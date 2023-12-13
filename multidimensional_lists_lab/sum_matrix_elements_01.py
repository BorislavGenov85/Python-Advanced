row, col = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for _ in range(row):
    elements = [int(x) for x in input().split(", ")]
    value = sum(elements)
    matrix.append(elements)
    total_sum += value
print(total_sum)
print(matrix)
