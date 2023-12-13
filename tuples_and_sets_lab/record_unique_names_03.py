number = int(input())
names = set()
for _ in range(number):
    line = input()
    names.add(line)

for name in names:
    print(name)
