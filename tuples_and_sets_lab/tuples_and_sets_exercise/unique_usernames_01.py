num = int(input())
names = set()
for _ in range(num):
    name = input()
    names.add(name)

names = list(names)
names_str = '\n'.join(names)
print(names_str)
