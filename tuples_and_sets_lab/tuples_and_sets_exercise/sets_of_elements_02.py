line = input().split()
num_1 = int(line[0])
num_2 = int(line[1])

set_1 = set()
set_2 = set()

for _ in range(num_1):
    data = int(input())
    set_1.add(data)
for _ in range(num_2):
    data = int(input())
    set_2.add(data)

unique = set_1 & set_2
for el in unique:
    print(el)
