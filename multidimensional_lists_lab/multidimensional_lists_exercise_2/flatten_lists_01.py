data = input().split("|")

matrix = []

for i in range(len(data) - 1, -1, -1):
    el = data[i].strip().split()
    matrix.extend(el)

print(*matrix)

# second solution
# data = input().split("|")
#
# matrix = []
#
# for el in range(len(data) - 1, -1, -1):
#     matrix.extend([x for x in data[el].split()])
# print(*matrix)
