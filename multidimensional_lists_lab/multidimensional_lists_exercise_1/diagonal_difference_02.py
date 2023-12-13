n = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][n - 1 - idx])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)
